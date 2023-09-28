<?php

namespace App\Http\Middleware;
use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Http;

class UserLog
{
    /**
     * Get the path the user should be redirected to when they are not authenticated.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return string|null
     */
    public function handle(Request $request, Closure $next)
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $genres = $request->all();
            $movieId = $genres["genreName"];
            $action = "genre";
        }
        if ($_SERVER['REQUEST_METHOD'] === 'GET') {
            $url = $_SERVER['REQUEST_URI']; 
            $movieId = basename($url);
            $action = "movieId";
        }
        $data = [
            'userId' => Auth::check()?Auth::user()->id:$request->session()->get('temp_user_id'),
            'actionEvent' =>  $action,
            'movieId' => $movieId,
            'rating' =>'',
            'recommendedMovies' => '',
        ];

        $response = Http::post('http://127.0.0.1:5000/api/userLog/add', $data);

        return $next($request);
    }
}
