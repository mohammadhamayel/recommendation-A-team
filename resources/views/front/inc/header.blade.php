<!-- header -->
<header class="header">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <nav class="header__content">
                    <!-- header logo -->
                    <a href="{{route('front.index')}}" class="header__logo">
                        <img src="{{asset('front/img/logo.svg')}}" alt="">
                    </a>
                    <!-- end header logo -->

                    <!-- header nav -->
                    <ul class="header__nav">

                        <li class="header__nav-item">
                            <a href="{{route('front.index')}}" class="header__nav-link">Home</a>
                        </li>


                        <!-- dropdown -->
                        <li class="header__nav-item d-none">
                            <a class="dropdown-toggle header__nav-link" href="#" role="button" id="dropdownMenuHome" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Catalog <i class="icon ion-ios-arrow-down"></i></a>

                            <ul class="dropdown-menu header__dropdown-menu" aria-labelledby="dropdownMenuHome">
                                <li><a href="#">Action</a></li>
                                <li><a href="#">Adventure</a></li>
                                <li><a href="#">Terror</a></li>
                            </ul>
                        </li>
                        <!-- end dropdown -->

                        @guest()
                            <li class="header__nav-item">
                                <a href="#" class="header__nav-link">Plans</a>
                            </li>
                        @endguest

                        @auth()
                            <!-- dropdown -->
                            <li class="header__nav-item d-none">
                                <a class="dropdown-toggle header__nav-link" href="#" role="button" id="dropdownMenuHome" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">My account <i class="icon ion-ios-arrow-down"></i></a>

                                <ul class="dropdown-menu header__dropdown-menu" aria-labelledby="dropdownMenuHome">
                                    <li><a href="{{route('front.auth.profile')}}">My profile</a></li>
                                    <!-- <li><a href="#">My videos</a></li> -->
                                </ul>
                            </li>
                            <!-- end dropdown -->
                        @endauth


                    </ul>
                    <!-- end header nav -->

                    <!-- header auth -->
                    <div class="header__auth">
                        <form action="#" class="header__search">
                            <input class="header__search-input d-none" type="text" placeholder="Pesquisar...">
                            <button class="header__search-button d-none" type="button">
                                <i class="icon ion-ios-search"></i>
                            </button>
                            <button class="header__search-close d-none" type="button">
                                <i class="icon ion-md-close"></i>
                            </button>
                        </form>

                        <button class="header__search-btn" type="button">
                            <i class="icon ion-ios-search"></i>
                        </button>

                        @guest()
                        <a href="{{route('front.login')}}" class="header__sign-in" title="Entrar">
                            <i class="icon ion-ios-log-in"></i>
                            <span>Log in</span>
                        </a>
                        @endguest

                        @auth()
                        <a href="{{route('front.logout')}}" class="header__sign-in" title="Sair">
                            <i class="icon ion-ios-log-out" style="transform: rotateZ(180deg)"></i>
                            <span>Log out</span>
                        </a>
                        @endauth
                    </div>
                    <!-- end header auth -->

                    <!-- header menu btn -->
                    <button class="header__btn" type="button">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                    <!-- end header menu btn -->
                </nav>
            </div>
        </div>
    </div>
</header>
<!-- end header -->
