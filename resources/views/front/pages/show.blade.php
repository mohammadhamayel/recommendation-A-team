@extends('layout.front')

@section('title', $movie['title'] )

@section('content')

    <div class="movie-info">   <!-- Movie-Info-Start -->
        <div class="container mx-auto px-4 py-16 flex flex-col md:flex-row">
            <div class="row">
                <div class="col-md-4">
                    <img src="{{ $movie['poster_path']  }}" alt="Poster" class="image-view">
                </div>
                <div class="col-md-8 text-white">
                    <h2 class="text-4xl md:mt-0 font-semibold">
                        {{ $movie['title'] }}
                    </h2>
                    {{-- Details --}}
                    <div class="flex flex-wrap items-center text-gray-600 text-sm">
                        <span id="rating" class="movie-details  text-gray-600">
                            <svg class="fill-current text-yellow-300 w-4" viewBox="0 0 24 24"><g data-name="Layer 2"><path d="M17.56 21a1 1 0 01-.46-.11L12 18.22l-5.1 2.67a1 1 0 01-1.45-1.06l1-5.63-4.12-4a1 1 0 01-.25-1 1 1 0 01.81-.68l5.7-.83 2.51-5.13a1 1 0 011.8 0l2.54 5.12 5.7.83a1 1 0 01.81.68 1 1 0 01-.25 1l-4.12 4 1 5.63a1 1 0 01-.4 1 1 1 0 01-.62.18z" data-name="star"/></g></svg>
                        </span>
                        <span class="ml-1">{{ $movie['vote_average'] }}</span>
                        <span class="mx-2">|</span>
                        <span>{{ $movie['release_date'] }}</span>
                        <span class="mx-2">|</span>
                        <span>
                                {{ $movie['genres'] }}
                        </span>
                        
                    </div>
                        <p class="text-gray-600 mt-3">
                            {{ $movie['overview'] }}
                        </p>
                        <div class="mt-5">
                            <h4 class="text-teal-400">Featured Cast</h4>
                            <div class="row m-0 mt-3 text-gray-600">
                                @foreach ($movie['featuredCast'] as $cast)
                                        <div class="mr-3">
                                            <div>{{ $cast['name'] }}</div>
                                         </div>
                                @endforeach
                            </div>
                        <div class="mt-4">
                            <h4 class="text-teal-400">Crew</h4>
                            <div class="row m-0 mt-3 text-gray-600">
                                @foreach ($movie['crew'] as $crew)
                                        <div class="mr-3">
                                            <div>{{ $crew['name'] }}</div>
                                            <div class="text-sm text-gray-400">{{ $crew['job'] }}</div>
                                         </div><br>
                                @endforeach
                            </div>
                        </div>
                        <div class="mt-5">
                            <h4 class="text-teal-400">Rate Me</h4>
                            <div class="rating mt-2">
                                <i class="rating__star far fa-star" onclick="getStars()"></i>
                                <i class="rating__star far fa-star" onclick="getStars()"></i>
                                <i class="rating__star far fa-star" onclick="getStars()"></i>
                                <i class="rating__star far fa-star" onclick="getStars()"></i>
                                <i class="rating__star far fa-star" onclick="getStars()"></i>
                            </div>
                            <div class="mt-1">
                                <p class="rateState red v-none" id="rateState">Please Select a Rate</p>
                            </div>
                            <div class="mt-3">
                                <button
                                    onclick="sendRate()"
                                    class="inline-flex items-center bg-teal-400 text-white rounded font-semibold px-4 py-3 hover:bg-teal-600 transition ease-in-out duration-150">
                                    <span class="ml-2">Send Rate</span>
                                </button>
                            </div>
                        <div class="mt-4">
                        
                        <div x-data="{ isOpen: false }">

                            {{-- Check if there is a video --}}
                            @if (false && count($movie['videos']['results']) > 0)
                                <div class="mt-5">
                                    <button
                                        @click="isOpen = true"
                                        class="inline-flex items-center bg-teal-400 text-white rounded font-semibold px-4 py-3 hover:bg-teal-600 transition ease-in-out duration-150">
                                        <svg class="w-6 fill-current" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M10 16.5l6-4.5-6-4.5v9zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
                                        <span class="ml-2">Play Trailer</span>
                                    </button>
                                </div>
                            <!-- Play Trailer Modal -->
                                <template x-if="isOpen">
                                    <div
                                        style="background-color: rgba(0, 0, 0, .5);"
                                        class="fixed top-0 left-0 w-full h-full flex items-center shadow-lg overflow-y-auto"
                                        x-show.transition.opacity="isOpen">
                                        <div class="container mx-auto lg:px-32 rounded-lg overflow-y-auto">
                                            <div class="bg-gray-600 rounded">
                                                <div class="flex justify-end pr-4 pt-2">
                                                    <!-- Close Button -->
                                                    <button
                                                        @click="isOpen = false"
                                                        @keydown.escape.window="isOpen = false"
                                                        class="text-3xl leading-none hover:text-gray-300">&times;
                                                    </button>
                                                </div>
                                                <div class="modal-body px-8 py-8">
                                                    <!-- Make YouTube Embed responsive -->
                                                    <div class="responsive-container overflow-hidden relative" style="padding-top: 56.25%">
                                                        <iframe class="responsive-iframe absolute top-0 left-0 w-full h-full" src="https://www.youtube.com/embed/{{ $movie['videos']['results'][0]['key'] }}" style="border:0;" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </template>
                            @endif
                        </div>
                </div>
            </div>
                
        </div>
    </div>
    <!-- Movie-Info-Ends -->

    <!-- cast-start -->
    <div class="movie-cast border-b border-t border-teal-400">
        <div class="container mx-auto px-4 py-16">
            <h2 class="text-4xl font-semibold text-wight text-white">Cast</h2>
            <div class="row">
             <!-- Dynamic Content from IMDB APi -->
            @foreach ($movie['cast'] as $cast)
                <div class="col-md-2 col-sm-4">
                    {{-- Image --}}
                    <a href="#">
                        <img src="{{ 'https://image.tmdb.org/t/p/w500/'.$cast['profile_path']  }}" alt="actor-photo" class="hover:opacity-75 transition ease-in-out duration-150 box-image">
                    </a>
                    {{-- Details --}}
                    <div class="mt-2">
                        <a href="#" class="text-lg mt-2 hover:text-gray:300">{{ $cast['name'] }}</a>
                        <div class="text-sm text-gray-400">
                            {{ $cast['character'] }}
                        </div>
                    </div>
                </div>
             @endforeach
        </div>
        </div>
    </div>
    <!-- cast-ends -->

    <!-- movie images-start -->
    <div class="movie-images border-b border-teal-400" x-data="{ isOpen: false, image: ''}">
        <div class="container mx-auto px-4 py-16">
            <h2 class="text-4xl font-semibold px-4 py-16 text-white">Images</h2>

            <div class="row">
                @foreach ($movie['images'] as $image)
                    <div class="col-md-4 col-sm-6 mt-2">
                        <a href="#"
                            @click.prevent="isOpen = true
                            image='{{ 'https://image.tmdb.org/t/p/original/'.$image['file_path'] }}'">
                            <img src="{{ 'https://image.tmdb.org/t/p/w500/'.$image['file_path']  }}" alt="movie-image" class="hover:opacity-75 transition ease-in-out duration-150 box-image">
                        </a>
                    </div>
                @endforeach
            </div>
            <!-- View Image Modal -->
            @if(false)
            <div
                style="background-color: rgba(0, 0, 0, .5);"
                class="fixed top-0 left-0 w-full h-full flex items-center shadow-lg overflow-y-auto"
                x-show="isOpen">
                <div class="container mx-auto lg:px-32 rounded-lg overflow-y-auto">
                    <div class="bg-gray-600 rounded">
                        <div class="flex justify-end pr-4 pt-2">
                            <button
                                @click="isOpen = false"
                                @keydown.escape.window="isOpen = false"
                                class="text-3xl leading-none hover:text-gray-300">&times;
                            </button>
                        </div>
                        <div class="modal-body px-8 py-8">
                            <img :src="image" alt="poster">
                        </div>
                    </div>
                </div>
            </div>
            @endif
    </div>
    <!-- movie images-end -->

    <!-- similar movie  -->
    <section class="home">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h1 class="home__title"><b>Similar</b> Movies</h1>

                    <button class="recommend__nav recommend__nav--prev" type="button" data-nav="#recommend_videos">
                        <i class="icon ion-ios-arrow-round-back"></i>
                    </button>
                    <button class="recommend__nav recommend__nav--next" type="button" data-nav="#recommend_videos">
                        <i class="icon ion-ios-arrow-round-forward"></i>
                    </button>
                </div>

                <div class="col-12">
                    <div class="owl-carousel recommend__carousel recommend__carousel--bg" id="recommend_videos">
                        {{-- Popular/Trending Movie Single container --}}
                            {{-- Dynamic Content From TMDB API --}}
                        @foreach ($popularMovies as $movie)
                            <x-MovieCardCpy :movie="$movie"/>
                        @endforeach
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- similar movie end -->

@endsection
<script>
    function getStars(){
        const ratingStars = [...document.getElementsByClassName("rating__star")];
        executeRating(ratingStars);
    }

    function executeRating(stars) {
        const starClassActive = "rating__star fas fa-star";
        const starClassInactive = "rating__star far fa-star";
        const starsLength = stars.length;
        let i;
        stars.map((star) => {
            star.onclick = () => {
            i = stars.indexOf(star);

            if (star.className===starClassInactive) {
                for (i; i >= 0; --i) stars[i].className = starClassActive;
            } 
            else {
                for (i; i < starsLength; ++i) stars[i].className = starClassInactive;
            }
            };
        });
    }

    function sendRate(){
        let rating = document.getElementsByClassName("fas").length;
        
        if(rating < 1){
            document.getElementById("rateState").classList.remove("v-none");
            return;
        }else
            document.getElementById("rateState").classList.add("v-none");

        $.post('{{ route('front.movies.rate') }}', {_token:'{{ csrf_token() }}', rate:rating}, function(data){
            console.log('data',data);
        });
    }

</script>