<?php

namespace App\Http\Controllers\Front;

use Exception;
use App\Models\Plan;
use App\Models\User;
use App\Models\UserPlan;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;
use App\Http\Requests\Auth\ChangeProfileRequest;
use App\Http\Requests\Auth\ChangePasswordRequest;
use App\Notifications\Subscriptions\CanceledSubscription;
use App\Notifications\Subscriptions\CreatedSubscription;
use Illuminate\Support\Facades\Http;
use App\ViewModels\MoviesViewModel;
use App\ViewModels\MovieViewModel;
use App\ViewModels\GenreViewModel;
use App\ViewModels\MoviesRecommendViewModel;

class FrontController extends Controller
{
    public function index(Request $request) {

        if(session()->has('checkout_plan')){

            $plan = session()->get('checkout_plan');
            session()->forget('checkout_plan');
            session()->save();

            return response()->json(['redirect' => route('front.checkout', $plan->id)], 200);
        }
        
    

        $popularMovies = Http::withToken(config('services.tmdb.token'))
         ->get('http://127.0.0.1:5000/api/movies/top10RatedMovies')
         ->json(['results']);

        $nowPlayingMovies = Http::withToken(config('services.tmdb.token'))
            ->get('http://127.0.0.1:5000/api/movies/top10NewMovies')
            ->json()['results'];
        // Get Genres
        $genres = Http::withToken(config('services.tmdb.token'))
            ->get('https://api.themoviedb.org/3/genre/movie/list')
            ->json(['genres']);

        $firstGenre = Http::withToken(config('services.tmdb.token'))
            ->get('http://127.0.0.1:5000/api/movies/top10PerGenre/drama')
            ->json()['results'];


        // Http Client From themoviedb, get popular movies from api
        //  $popularMovies = Http::withToken(config('services.tmdb.token'))
        //  ->get('https://api.themoviedb.org/3/movie/popular')
        //  ->json(['results']);

        // Http Client From themoviedb, get now playing movies from api
        // $nowPlayingMovies = Http::withToken(config('services.tmdb.token'))
        //     ->get('https://api.themoviedb.org/3/movie/now_playing')
        //     ->json()['results'];
        if(Auth::check()){
        // Http Client From themoviedb, get recommend playing movies from api
            // $recommendMovies = Http::withToken(config('services.tmdb.token'))
            //     ->get('http://127.0.0.1:5000/api/movies/top10NewMovies')
            //     ->json(['results']);

            $recommendMovies = Http::withToken(config('services.tmdb.token'))
                ->get('http://127.0.0.1:5000/api/movies/top10PerGenre/crime')
                ->json(['results']);
            $viewModel = new MoviesRecommendViewModel(
                $recommendMovies,
                $popularMovies,
                $nowPlayingMovies,
                $genres,
                $firstGenre
            );
        }else{
            $viewModel = new MoviesViewModel(
                $popularMovies,
                $nowPlayingMovies,
                $genres,
                $firstGenre
            );
        }
        
        if(!$request->session()->get('temp_user_id')){
            $randNum = time() + rand() ;
            $request->session()->put('temp_user_id', intval(substr(time() + rand(),0,9)));
        }
            
        return view('front.pages.index',$viewModel);
    }

    public function login() {
        if(Auth::check()) return redirect()->route('front.index');
        return view('front.pages.login');
    }

    public function register() {
        if(Auth::check()) return redirect()->route('front.index');
        return view('front.pages.register');
    }

    public function profile() {
        if(!Auth::check()) return redirect()->route('front.login');
        return view('front.pages.user.profile');
    }

    public function checkout(Plan $plan){

        if(User::find(Auth::id())->isAdmin()){
            return abort(403, 'This is not for you!');
        }

        $user = User::find(Auth::id());

        if(!Auth::check()){
            session('checkout_plan', $plan);
            session()->put('checkout_plan', $plan);
            session()->save();
            return redirect()->route('front.login');
        }

        $intent = $user->createSetupIntent();

        return view('front.pages.checkout', compact('plan', 'intent'));
    }

    public function checkoutProcess(Request $request){

        DB::beginTransaction();
        try{

            $user = User::find(Auth::id());
            $user->createOrGetStripeCustomer();

            $intent = $request->intent;
            $plan = $request->plan;
            $plan = decrypt($plan);

            if (!$user->hasDefaultPaymentMethod()) {
                $user->updateDefaultPaymentMethod($intent['payment_method']);
            }

            $plan = Plan::find($plan);

            if($plan->value == 0){
                $this->setFreePlan($plan, $user);
            }else{
                $this->setStripePlan($plan, $user, $intent);
            }

            $user->notify(new CreatedSubscription($plan));

            DB::commit();
            return response()->json(['success']);

        }catch(Exception $e){

            DB::rollBack();

            Log::error('Error', ['Error' => 'Checkout', 'message' => $e]);
            return response()->json(['error' => ['message' => 'unexpected error!']], 500);

        }

    }

    public function changePassword(ChangePasswordRequest $request){
        if(!Auth::check()) {
            return response()->json(['redirect' => true, 'redirectUrl' => route('front.login')], 401);
        }

        $current_password = $request->current_password;
        if(!Hash::check($current_password, Auth::user()->getAuthPassword())){
            return response()->json(['message' => 'This password appears to be incorrect!'], 401);
        }

        DB::beginTransaction();
        try{
            $user = User::findOrFail(Auth::id());
            $user->update([
                'password' => Hash::make($request->new_password)
            ]);

            DB::commit();
            return response()->json(['message' => 'Password modified successfully!']);

        }catch(Exception $e){

            DB::rollBack();
            return response()->json(['message' => $e->getMessage()], 500);

        }

    }

    public function changeProfile(ChangeProfileRequest $request){
        if(!Auth::check()) {
            return response()->json(['redirect' => true, 'redirectUrl' => route('front.login')], 401);
        }

        try{

            DB::beginTransaction();

            $user = User::findOrFail(Auth::id());
            $user->update([
                'name' => $request->name,
                'last_name' => $request->last_name
            ]);

            DB::commit();
            return response()->json(['message' => 'Data modified successfully!']);

        }catch(Exception $e){

            DB::rollBack();
            return response()->json(['message' => $e->getMessage()], 500);

        }


    }

    protected function setFreePlan($plan, $user){
        $plan_slug = Str::slug($plan->id .' & '. $plan->title);

        if ($user->subscribed($plan_slug)) {
            $user->subscription($plan_slug)->cancelNow();
            $user->notify(new CanceledSubscription($plan));
        }
        UserPlan::where('user_id', Auth::id())->update(['active' => false]);

        UserPlan::create([
            'plan_id' => $plan->id,
            'user_id' => Auth::id(),
            'payment_getaway' => 'stripe',
            'payment_value' => $plan->value,
            'payment_date' => now(),
            'start' => now(),
            'end' => null,
            'active' => true
        ]);
    }

    protected function setStripePlan($plan, $user, $intent){
        $plan_slug = Str::slug($plan->id .' & '. $plan->title);

        if ($user->subscribed($plan_slug)) {
            $user->subscription($plan_slug)->cancelNow();
            $user->notify(new CanceledSubscription($plan));
        }

        if(!$plan->stripe_link){
            Log::error('Stripe Link', ['Error' => 'Plan not synced!', 'Plano' => $plan]);
            return response()->json(['error' => ['message' => 'unexpected error!']], 500);
        }

        $user->newSubscription(
            $plan_slug, $plan->stripe_link
        )->create($intent['payment_method'], [
            'email' => $user->email,
        ]);

        UserPlan::where('user_id', Auth::id())->update(['active' => false]);

        UserPlan::create([
            'plan_id' => $plan->id,
            'user_id' => Auth::id(),
            'payment_getaway' => 'stripe',
            'payment_value' => $plan->value,
            'payment_date' => now(),
            'start' => now(),
            'end' => now()->addMonths($plan->period),
            'active' => true
        ]);
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        
        // $similarMovies = Http::withToken(config('services.tmdb.token'))
        // ->get('https://api.themoviedb.org/3/movie/popular')
        // ->json(['results']);
        $similarMovies = Http::withToken(config('services.tmdb.token'))
        ->get('http://127.0.0.1:5000/api/recommendation/perMovie/',$id)
        ->json(['results']);
        
        $movie = Http::withToken(config('services.tmdb.token'))
            ->get('https://api.themoviedb.org/3/movie/'.$id.'?append_to_response=credits,videos,images')
            ->json();

        $genres = Http::withToken(config('services.tmdb.token'))
            ->get('https://api.themoviedb.org/3/genre/movie/list')
            ->json(['genres']);
        $viewModel = new MovieViewModel($movie,$similarMovies,$genres);

        return view('front.pages.show', $viewModel);
    }

    /**
     * Display the specified resource.
     *
     * @param  Request $request
     * @return \Illuminate\Http\Response
     */
    public function rate(Request $request)
    {
        $rate = $request->rate;
        $movieId = $request->movieId;

        $data = [
            'userId' => Auth::check()?Auth::user()->id:$request->session()->get('temp_user_id'),
            'actionEvent' => 'rate',
            'movieId' => $movieId,
            'rating' => $rate,
            'recommendedMovies' => '',
        ];

        $response = Http::post('http://127.0.0.1:5000/api/userLog/add', $data);
        if($response['code'] != 0){
            Log::error('user rating', ['Error' => 'user not synced!', 'user' => $response]);
        }
        return array(
            'status' => 1,
            'message' => "success"
        );
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function getMoviesPerGenre(Request $request)
    {
        $genreName = $request->genreName;
        // Http Client From themoviedb, get genre movies from api
        // $nowPlayingMovies = Http::withToken(config('services.tmdb.token'))
        //     ->get('https://api.themoviedb.org/3/movie/now_playing')
        //     ->json()['results'];

        $genreMovie = Http::withToken(config('services.tmdb.token'))
         ->get('http://127.0.0.1:5000/api/movies/top10PerGenre/'.$genreName)
         ->json(['results']);

         if(!$genreMovie){
            return response()->json(false);;
         }

        $genres = Http::withToken(config('services.tmdb.token'))
        ->get('https://api.themoviedb.org/3/genre/movie/list')
        ->json(['genres']);

        $viewModel = new GenreViewModel($genreMovie,$genres);
        $viewRendered = view('components.moviecardPerGenre', compact('viewModel'))->render();
        return response()->json(['html'=>$viewRendered]);
    }
}
