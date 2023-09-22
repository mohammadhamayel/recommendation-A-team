@extends('layout.front')
@section('content')
    <section class="sign section--bg" data-bg="{{asset('front/img/section.jpg')}}">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="sign__content">
                        <form action="{{route('front.do.login')}}" method="POST" class="sign__form" id="sign___form">
                            @csrf
                            <a href="{{route('front.login')}}" class="sign__logo">
                                <img src="{{asset('front/img/logo.svg')}}" alt="">
                            </a>

                            <div class="sign__group">
                                <input type="email" name="email" class="sign__input" value="" placeholder="Email" required>
                            </div>

                            <div class="sign__group">
                                <input type="password" name="password" class="sign__input" value="" placeholder="password" required>
                            </div>

                            <button class="sign__btn" type="submit">Access</button>

                            <span class="sign__delimiter">or</span>

                            <span class="sign__text">Don't have an account? <a href="{{route('front.register')}}">Register!</a></span>

                            <span class="sign__text d-none"><a href="#">Forgot your password?</a></span>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

@endsection

@push('scripts')
    @vite('resources/js/auth/login.js')
@endpush
