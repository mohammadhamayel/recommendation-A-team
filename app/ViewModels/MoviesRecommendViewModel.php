<?php

namespace App\ViewModels;

use Carbon\Carbon;
use Spatie\ViewModels\ViewModel;

class MoviesRecommendViewModel extends ViewModel
{
    // ViewModel Variables
    public $popularMovies;
    public $nowPlayingMovies;
    public $genres;
    public $firstGenre;
    public $recommendMovies;

    // Constructor
    public function __construct($recommendMovies,$popularMovies,$nowPlayingMovies,$genres,$firstGenre)
    {
        $this->recommendMovies = $recommendMovies;
        $this->popularMovies = $popularMovies;
        $this->nowPlayingMovies = $nowPlayingMovies;
        $this->genres = $genres;
        $this->firstGenre = $firstGenre;
    }

    // Getters
    public function recommendMovies(){
        return $this->formatMovies($this->recommendMovies);
    }
    public function popularMovies(){
        return $this->formatMovies($this->popularMovies);
    }
    public function nowPlayingMovies(){
        return $this->formatMovies($this->nowPlayingMovies);
    }
    public function genres(){
            return  $genres = collect($this->genres)->mapWithKeys(function ($genre){
                return[$genre['id'] =>$genre['name']];
            });
    }
    public function firstGenre(){
        return $this->formatMovies($this->firstGenre);
    }

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
