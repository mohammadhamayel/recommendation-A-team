from typing import List, Optional


class Movie:
    def __init__(self, adult: bool, backdrop_path: Optional[str], release_date: str, genre_ids: List[int], id: int,
                 title: str, original_language: str, original_title: str,
                 overview: str, popularity: float, poster_path: Optional[str], vote_average: float,
                 vote_count: int):
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.release_date = release_date
        self.genre_ids = genre_ids
        self.id = id
        self.title = title
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.video = False


class MovieResponse:
    def __init__(self, page: int, results: List[Movie], total_pages: int, total_results: int):
        self.page = page
        self.results = results
        self.total_pages = total_pages
        self.total_results = total_results
