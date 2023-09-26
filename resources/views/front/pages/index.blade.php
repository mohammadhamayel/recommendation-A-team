@extends('layout.front')
@section('content')
    <!-- home -->
    <!-- Recommended Movies -->
    <section class="home">
        @if(Auth::check())
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h1 class="home__title"><b>Recommended</b> Movies</h1>

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
        @endif
    </section>

    <!-- Top Movies -->
    <section class="">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h1 class="home__title"><b>TOP</b> Movies</h1>

                    <button class="home__nav home__nav--prev" type="button" data-nav="#top_videos">
                        <i class="icon ion-ios-arrow-round-back"></i>
                    </button>
                    <button class="home__nav home__nav--next" type="button" data-nav="#top_videos">
                        <i class="icon ion-ios-arrow-round-forward"></i>
                    </button>
                </div>

                <div class="col-12">
                    <div class="owl-carousel home__carousel home__carousel--bg" id="top_videos">
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

    <!-- new videos -->
    <section class="new-videos">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h1 class="home__title"><b>NEW</b> Movies</h1>

                    <button class="new__nav new__nav--prev" type="button" data-nav="#new_videos">
                        <i class="icon ion-ios-arrow-round-back"></i>
                    </button>
                    <button class="new__nav new__nav--next" type="button" data-nav="#new_videos">
                        <i class="icon ion-ios-arrow-round-forward"></i>
                    </button>
                </div>

                <div class="col-12">
                    <div class="owl-carousel new__carousel new__carousel--bg" id="new_videos">
                        {{-- Popular/Trending Movie Single container --}}
                            {{-- Dynamic Content From TMDB API --}}
                        @foreach ($nowPlayingMovies as $movie)
                            <x-MovieCardCpy :movie="$movie"/>
                        @endforeach
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- end home -->

    <!-- content -->
    <section class="content">
        <div class="content__head">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <!-- content title -->
                        <h2 class="content__title">Genres</h2>
                        <!-- end content title -->

                        <!-- content tabs nav -->
                        <ul class="nav nav-tabs content__tabs" id="content__tabs" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" data-toggle="tab" href="#tab-1" role="tab" aria-controls="tab-1" aria-selected="true">RECENT</a>
                            </li>

                            <li class="nav-item">
                                <a class="nav-link" data-toggle="tab" href="#tab-2" role="tab" aria-controls="tab-2" aria-selected="false">ACTION</a>
                            </li>

                            <li class="nav-item">
                                <a class="nav-link" data-toggle="tab" href="#tab-3" role="tab" aria-controls="tab-3" aria-selected="false">ADVENTURE</a>
                            </li>

                            <li class="nav-item">
                                <a class="nav-link" data-toggle="tab" href="#tab-4" role="tab" aria-controls="tab-4" aria-selected="false">COMEDY</a>
                            </li>
                        </ul>
                        <!-- end content tabs nav -->

                        <!-- content mobile tabs nav -->
                        <div class="content__mobile-tabs" id="content__mobile-tabs">
                            <div class="content__mobile-tabs-btn dropdown-toggle" role="navigation" id="mobile-tabs" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <input type="button" value="New releases">
                                <span></span>
                            </div>

                            <div class="content__mobile-tabs-menu dropdown-menu" aria-labelledby="mobile-tabs">
                                <ul class="nav nav-tabs" role="tablist">
                                    <li class="nav-item"><a class="nav-link active" id="1-tab" data-toggle="tab" href="#tab-1" role="tab" aria-controls="tab-1" aria-selected="true">NEW RELEASES</a></li>

                                    <li class="nav-item"><a class="nav-link" id="2-tab" data-toggle="tab" href="#tab-2" role="tab" aria-controls="tab-2" aria-selected="false">MOVIES</a></li>

                                    <li class="nav-item"><a class="nav-link" id="3-tab" data-toggle="tab" href="#tab-3" role="tab" aria-controls="tab-3" aria-selected="false">TV SERIES</a></li>

                                    <li class="nav-item"><a class="nav-link" id="4-tab" data-toggle="tab" href="#tab-4" role="tab" aria-controls="tab-4" aria-selected="false">CARTOONS</a></li>
                                </ul>
                            </div>
                        </div>
                        <!-- end content mobile tabs nav -->
                    </div>
                </div>
            </div>
        </div>

        <div class="container">
            <!-- content tabs -->
            <div class="tab-content">
                <div class="tab-pane fade show active" id="tab-1" role="tabpanel" aria-labelledby="1-tab">
                    <div class="row row--grid">
                        <!-- card -->
                        <div class="col-6 col-sm-4 col-md-3 col-xl-2">
                            <x-MovieCard />
                        </div>
                        <!-- end card -->

                        <!-- card -->
                        <div class="col-6 col-sm-4 col-md-3 col-xl-2">
                            <x-MovieCard />
                        </div>
                        <!-- end card -->

                        <!-- card -->
                        <div class="col-6 col-sm-4 col-md-3 col-xl-2">
                            <x-MovieCard />
                        </div>
                        <!-- end card -->

                        <!-- card -->
                        <div class="col-6 col-sm-4 col-md-3 col-xl-2">
                            <x-MovieCard />
                        </div>
                        <!-- end card -->
                    </div>
                </div>

                <div class="tab-pane fade" id="tab-2" role="tabpanel" aria-labelledby="2-tab">
                    <div class="row row--grid">
                        <!-- card -->
                        <div class="col-6 col-sm-4 col-md-3 col-xl-2">
                            <x-MovieCard />
                        </div>
                        <!-- end card -->
                    </div>
                </div>

                <div class="tab-pane fade" id="tab-3" role="tabpanel" aria-labelledby="3-tab">
                    <div class="row row--grid">
                        <!-- card -->
                        <div class="col-6 col-sm-4 col-md-3 col-xl-2">
                            <x-MovieCard />
                        </div>
                        <!-- end card -->

                        <!-- card -->
                        <div class="col-6 col-sm-4 col-md-3 col-xl-2">
                            <x-MovieCard />
                        </div>
                        <!-- end card -->
                    </div>
                </div>

                <div class="tab-pane fade" id="tab-4" role="tabpanel" aria-labelledby="4-tab">
                    <div class="row row--grid">
                       <!-- section title -->
                        <div class="col-12">
                            <div class="section__title-wrap">
                                <h2 class="section__title"></h2>

                                <div class="section__nav-wrap">
                                    <a href="#" class="section__view">See all</a>

                                    <button class="section__nav section__nav--prev" type="button" data-nav="#carousel1">
                                        <i class="icon ion-ios-arrow-back"></i>
                                    </button>

                                    <button class="section__nav section__nav--next" type="button" data-nav="#carousel1">
                                        <i class="icon ion-ios-arrow-forward"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <!-- end section title -->

                        <!-- carousel -->
                        <div class="col-12">
                            <div class="owl-carousel section__carousel" id="carousel1">
                                @foreach ($popularMovies as $movie)
                                    <x-MovieCardCpy :movie="$movie"/>
                                @endforeach
                            </div>
                        </div>
                        <!-- carousel -->
                    </div>
                </div>
            </div>
            <!-- end content tabs -->
        </div>
    </section>
    <!-- end content -->

    @if(false)
    @guest()
        <!-- plans -->
        <section class="section section--border">
            <div class="container">
                <div class="row">
                    <div class="col-12 col-xl-10">
                        <h2 class="section__title section__title--mb"><b>Plans</b> – Check out our plans</h2>

                        <p class="section__text">
                            Lorem ipsum dolor sit amet, <b>consectetur adipiscing elit.</b> Quisque vitae felis efficitur justo dapibus dapibus.
                            Duis lacus lorem, commodo non lorem nec, porta viverra mauris. Sed consequat metus a dignissim semper.
                            Donec eu malesuada velit. Mauris fringilla erat id egestas congue. Praesent diam purus, suscipit et sodales sit amet,
                            tincidunt vel tortor. Maecenas at egestas purus. Integer ullamcorper fringilla ipsum vel finibus. Morbi scelerisque sit
                            amet augue volutpat vehicula. Sed viverra erat et sagittis iaculis. Vestibulum eu nunc lobortis, ullamcorper est convallis,
                            feugiat leo. Nam pretium ex metus, a gravida justo tincidunt nec. Duis condimentum enim nisl, sagittis condimentum orci
                            iaculis eget. Vivamus nunc mi, sodales luctus libero eu, faucibus fermentum mi. Ut arcu diam, molestie at dictum a,
                            tincidunt non diam. Duis vitae <a href="#">blandit leo.</a>
                        </p>
                    </div>
                </div>

                <x-plans />
            </div>
        </section>
        <!-- end plans -->
    @endguest
    @endif
@endsection
