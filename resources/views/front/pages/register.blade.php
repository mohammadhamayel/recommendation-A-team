@extends('layout.front')
@section('content')
    <section class="sign section--bg" data-bg="{{asset('front/img/section.jpg')}}">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="sign__content">
                        <form action="{{route('front.do.register')}}" method="POST" class="sign__form" id="sign___form">
                            @csrf
                            <a href="{{route('front.login')}}" class="sign__logo">
                                <img src="{{asset('front/img/logo.svg')}}" alt="">
                            </a>

                            <div class="sign__group">
								<input type="text" class="sign__input" placeholder="Nome" name="firstName" min="3" max="50" required>
							</div>

                            <div class="sign__group">
								<input type="text" class="sign__input" placeholder="Sobrenome" name="lastName" min="3" max="50" required>
							</div>

							<div class="sign__group">
								<input type="email" class="sign__input" placeholder="Email" name="email" min="6" max="191">
							</div>

							<div class="sign__group">
								<input type="password" class="sign__input" placeholder="Password" name="password" min="6" max="191">
							</div>

							<div class="sign__group sign__group--checkbox">
								<input id="remember" name="remember" type="checkbox" checked="checked">
								<label for="remember">I have read and agree with the <a href="#">privacy policies</a></label>
							</div>

							<button class="sign__btn" type="submit">Open account</button>

							<span class="sign__delimiter">or</span>

							<span class="sign__text">Already have an account? <a href="{{route('front.login')}}">Log in!</a></span>

                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
@endsection

@push('scripts')
    @vite('resources/js/auth/register.js')
@endpush
