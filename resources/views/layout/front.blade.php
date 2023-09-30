<!DOCTYPE html>
<html lang="en">
@include('front.inc.head')

<body class="body">
	@include('front.inc.header')

	@yield('content')

	@include('front.inc.footer')
    @include('front.inc.scripts')
	<div id="loaderContainer" class="">
		<div id="loader"></div>
	<div>
</body>

</html>
