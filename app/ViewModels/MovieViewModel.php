<?php

namespace App\ViewModels;

use Carbon\Carbon;
use Spatie\ViewModels\ViewModel;

class MovieViewModel extends ViewModel
{

    public $movie;
    // new added
    public $similars;
    public $genres;


    public function __construct($movie,$similars, $genres)
    {
        $this->movie = $movie;
        // new added
        $this->similars = $similars;
        $this->genres = $genres;
    }

    // new added
     // Getters
     public function popularMovies(){
        return $this->formatMovies($this->similars);
    }

    public function movie(){

        return collect($this->movie)->merge([
                'poster_path'=> 'https://image.tmdb.org/t/p/w500/'.$this->movie['poster_path'],
                'vote_average'=> $this->movie['vote_average'] * 10 .'%',
                'release_date' => Carbon::parse( $this->movie['release_date'])->format('d M, Y'),
                'genres' => collect($this->movie['genres'])->pluck('name')->flatten()->implode(', '),
                'featuredCast' => collect($this->movie['credits']['cast'])->take(4),
                'cast' => collect($this->movie['credits']['cast'])->take(8),
                'crew' => collect($this->movie['credits']['crew'])->take(4),
                'images' => collect($this->movie['images']['backdrops'])->take(9),

        ])->only([
            'poster_path', 'id', 'genres', 'title', 'vote_average', 'overview', 'release_date', 'credits' ,
            'videos', 'images', 'crew', 'cast', 'images', 'featuredCast',
        ]);
    }

    // new added
    public function genres(){
        return  $genres = collect($this->genres)->mapWithKeys(function ($genre){
            return[$genre['id'] =>$genre['name']];
    });
}
    // new added
    private function formatMovies($movies){

        return collect($movies)->map(function($movie){
           $genresFormatted = collect($movie['genre_ids'])->mapWithKeys(function($value){
               return [$value => $this->genres()->get($value)];
           })->implode(', ');

           return collect($movie)->merge([
               'poster_path'=> 'https://image.tmdb.org/t/p/w500/'.$movie['poster_path'],
               'vote_average'=> $movie['vote_average'] * 10 .'%',
               'release_date' => Carbon::parse( $movie['release_date'])->format('d M, Y'),
               'genres' => $genresFormatted,
           ])->only([
               'poster_path', 'id', 'genre_ids', 'title', 'vote_average', 'overview', 'release_date', 'genres',
           ]);
       });
   }

}
