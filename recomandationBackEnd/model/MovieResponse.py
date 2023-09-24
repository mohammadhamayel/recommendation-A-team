from typing import List, Optional


class Movie:
    def __init__(self, adult: bool, backdrop_path: Optional[str], first_air_date: str, genre_ids: List[int], id: int,
                 name: str, original_language: str, original_name: str,
                 overview: str, popularity: float, poster_path: Optional[str], vote_average: float,
                 vote_count: int):
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.first_air_date = first_air_date
        self.genre_ids = genre_ids
        self.id = id
        self.name = name
        self.original_language = original_language
        self.original_name = original_name
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.vote_average = vote_average
        self.vote_count = vote_count


class MovieResponse:
    def __init__(self, page: int, results: List[Movie], total_pages: int, total_results: int):
        self.page = page
        self.results = results
        self.total_pages = total_pages
        self.total_results = total_results
