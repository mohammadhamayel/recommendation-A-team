from marshmallow import Schema, fields


class MovieSchema(Schema):
    backdrop_path = fields.Str(allow_none=True)
    first_air_date = fields.Str()
    genre_ids = fields.List(fields.Int())
    id = fields.Int()
    name = fields.Str()
    origin_country = fields.List(fields.Str())
    original_language = fields.Str()
    original_name = fields.Str()
    overview = fields.Str()
    popularity = fields.Float()
    poster_path = fields.Str(allow_none=True)
    vote_average = fields.Float()
    vote_count = fields.Int()


class MovieResponseSchema(Schema):
    page = fields.Int()
    results = fields.Nested(MovieSchema(), many=True)
    total_pages = fields.Int()
    total_results = fields.Int()
