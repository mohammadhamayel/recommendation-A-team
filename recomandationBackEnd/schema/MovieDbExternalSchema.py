from marshmallow import Schema, fields


class BelongsToCollectionSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    poster_path = fields.Str()
    backdrop_path = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class ProductionCompanySchema(Schema):
    id = fields.Int()
    logo_path = fields.Str()
    name = fields.Str()
    origin_country = fields.Str()


class ProductionCountrySchema(Schema):
    iso_3166_1 = fields.Str()
    name = fields.Str()


class SpokenLanguageSchema(Schema):
    english_name = fields.Str()
    iso_639_1 = fields.Str()
    name = fields.Str()


class MovieExternalSchema(Schema):
    adult = fields.Boolean()
    backdrop_path = fields.Str()
    belongs_to_collection = fields.Nested(BelongsToCollectionSchema())
    budget = fields.Int()
    genres = fields.List(fields.Nested(GenreSchema()))
    homepage = fields.Str()
    id = fields.Int()
    imdb_id = fields.Str()
    original_language = fields.Str()
    original_title = fields.Str()
    overview = fields.Str()
    popularity = fields.Float()
    poster_path = fields.Str()
    production_companies = fields.List(fields.Nested(ProductionCompanySchema()))
    production_countries = fields.List(fields.Nested(ProductionCountrySchema()))
    release_date = fields.Str()
    revenue = fields.Int()
    runtime = fields.Int()
    spoken_languages = fields.List(fields.Nested(SpokenLanguageSchema()))
    status = fields.Str()
    tagline = fields.Str()
    title = fields.Str()
    video = fields.Boolean()
    vote_average = fields.Float()
    vote_count = fields.Int()


# Getter functions for field retrieval
def get_adult(movie_data):
    return movie_data.get("adult")


def get_backdrop_path(movie_data):
    return movie_data.get("backdrop_path")


def get_belongs_to_collection(movie_data):
    return movie_data.get("belongs_to_collection")


def get_budget(movie_data):
    return movie_data.get("budget")


def get_genres(movie_data):
    return movie_data.get("genres")


def get_homepage(movie_data):
    return movie_data.get("homepage")


def get_id(movie_data):
    return movie_data.get("id")


def get_imdb_id(movie_data):
    return movie_data.get("imdb_id")


def get_original_language(movie_data):
    return movie_data.get("original_language")


def get_original_title(movie_data):
    return movie_data.get("original_title")


def get_overview(movie_data):
    return movie_data.get("overview")


def get_popularity(movie_data):
    return movie_data.get("popularity")


def get_poster_path(movie_data):
    return movie_data.get("poster_path")


def get_production_companies(movie_data):
    return movie_data.get("production_companies")


def get_production_countries(movie_data):
    return movie_data.get("production_countries")


def get_release_date(movie_data):
    return movie_data.get("release_date")


def get_revenue(movie_data):
    return movie_data.get("revenue")


def get_runtime(movie_data):
    return movie_data.get("runtime")


def get_spoken_languages(movie_data):
    return movie_data.get("spoken_languages")


def get_status(movie_data):
    return movie_data.get("status")


def get_tagline(movie_data):
    return movie_data.get("tagline")


def get_title(movie_data):
    return movie_data.get("title")


def get_video(movie_data):
    return movie_data.get("video")


def get_vote_average(movie_data):
    return movie_data.get("vote_average")


def get_vote_count(movie_data):
    return movie_data.get("vote_count")
