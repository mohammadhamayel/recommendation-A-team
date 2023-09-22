<?php

namespace App\ViewModels;

use Illuminate\Support\Carbon;
use Spatie\ViewModels\ViewModel;

class TvShowViewModel extends ViewModel
{
    public $tvshow;

    public function __construct($tvshow)
    {
        $this->tvshow = $tvshow;
    }

    public function tvshow(){

        return collect($this->tvshow)->merge([
                'poster_path'=> 'https://image.tmdb.org/t/p/w500/'.$this->tvshow['poster_path'],
                'vote_average'=> $this->tvshow['vote_average'] * 10 .'%',
                'first_air_date' => Carbon::parse( $this->tvshow['first_air_date'])->format('d M, Y'),
                'genres' => collect($this->tvshow['genres'])->pluck('name')->flatten()->implode(', '),
                'featuredCast' => collect($this->tvshow['credits']['cast'])->take(4),
                'cast' => collect($this->tvshow['credits']['cast'])->take(8),
                'crew' => collect($this->tvshow['credits']['crew'])->take(4),
                'images' => collect($this->tvshow['images']['backdrops'])->take(9),

        ])->only([
            'poster_path', 'id', 'genres', 'name', 'vote_average', 'overview', 'first_air_date', 'credits' ,
            'videos', 'images', 'crew', 'cast', 'images', 'featuredCast', 'created_by',
        ]);
    }
}
