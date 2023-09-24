from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BelongsToCollection:
    id: int
    name: str
    poster_path: str
    backdrop_path: str


@dataclass
class Genre:
    id: int
    name: str


@dataclass
class ProductionCompany:
    id: int
    logo_path: str
    name: str
    origin_country: str


@dataclass
class ProductionCountry:
    iso_3166_1: str
    name: str


@dataclass
class SpokenLanguage:
    english_name: str
    iso_639_1: str
    name: str


@dataclass
class MovieExternalModel:
    adult: bool
    backdrop_path: str
    budget: int
    id: int
    imdb_id: str
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    revenue: int
    runtime: int
    status: str
    tagline: str
    title: str
    video: bool
    vote_average: float
    vote_count: int
    release_date: str
    genres: List[Genre] = field(default_factory=list)
    spoken_languages: List[SpokenLanguage] = field(default_factory=list)
    belongs_to_collection: Optional[BelongsToCollection] = None
    homepage: Optional[str] = None
    production_companies: List[ProductionCompany] = field(default_factory=list)
    production_countries: List[ProductionCountry] = field(default_factory=list)
