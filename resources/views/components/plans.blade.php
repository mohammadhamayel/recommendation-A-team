<div class="row row--grid">
    @forelse ($plans as $plan)
        <!-- price -->
        <div class="{{ $class }} {{$checkout ? 'p-1' : ''}}">
            <div class="price {{ $plan->value != 0 ? 'price--premium' : '' }}  {{$checkout ? 'm-0' : ''}}">

                <div class="price__item price__item--first"><span>{{$plan->title}}</span> <span>{{ $plan->value != 0 ? 'R$ ' . number_format($plan->value, 2, ',', '.') : 'Free' }}</span></div>
                <div class="price__item"><span><i class="icon ion-ios-checkmark"></i> {{ $plan->period != 0 ? ($plan->period > 1 ? 'to each '. $plan->period .' meses': 'Todo mês') : 'S/term' }} </span></div>
                <div class="price__item"><span><i class="icon ion-ios-checkmark"></i> Até {{ $plan->configuration['video_size'] == 'infinite' ? '4K' : $plan->configuration['video_size'] }}</span></div>

                @if($plan->configuration['rating'] == 'true')
                    <div class="price__item"><span><i class="icon ion-ios-checkmark"></i> Assessments</span></div>
                @else
                    <div class="price__item price__item--none"><span><i class="icon ion-ios-close"></i> Assessments</span></div>
                @endif

                @if($plan->configuration['comments'] == 'true')
                    <div class="price__item"><span><i class="icon ion-ios-checkmark"></i> Comments</span></div>
                @else
                    <div class="price__item price__item--none"><span><i class="icon ion-ios-close"></i> Comments</span></div>
                @endif

                @if($plan->configuration['upload_download'] == 'true')
                    <div class="price__item"><span><i class="icon ion-ios-checkmark"></i> Upload/Download videos</span></div>
                @else
                    <div class="price__item price__item--none"><span><i class="icon ion-ios-close"></i> Upload/Download videos</span></div>
                @endif

                @if($plan->configuration['support'] == 'true')
                    <div class="price__item"><span><i class="icon ion-ios-checkmark"></i> No Support</span></div>
                @else
                    <div class="price__item price__item--none"><span><i class="icon ion-ios-close"></i> No Support</span></div>
                @endif

                @if(!$checkout)
                    <a href="{{ route('front.checkout', $plan->id) }}" class="price__btn">Choose plan</a>
                @endif

            </div>
        </div>
        <!-- end price -->
    @empty
        <div class="col-12 col-md-6 col-lg-4 my-4">
            <p style="color: white;">No plans to be activated at this time!</p>
        </div>
    @endforelse
</div>
