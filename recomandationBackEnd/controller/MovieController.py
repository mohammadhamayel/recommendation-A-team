from sqlalchemy import text

from recomandationBackEnd import db
from recomandationBackEnd.controller.MovieDbExternalProxy import get_movie_info
from recomandationBackEnd.model.MovieResponse import MovieResponse, Movie


def top10RatedMovies():

    engine = db.get_engine()
    query = text("""
            SELECT m.MovieID As MovieID,m.Title As Title, COUNT(r.Rating) AS RatingCount, AVG(r.Rating) AS AvgRating , m.tmdbId As tmdbId
            FROM movies m
            JOIN ratings r ON m.MovieID = r.MovieID
            WHERE r.Rating > 4
            GROUP BY m.MovieID, m.Title,m.tmdbId
            ORDER BY RatingCount DESC
            LIMIT 10;
        """)
    with engine.connect() as connection:
        result = connection.execute(query)

    # Create a list to store movie data
    movie_data_list = []
    # Iterate over the query result and create a list of movie data
    for row in result:
        tmdb_id = row[4]
        # Use the tmdb_id to retrieve additional movie information using the MovieSchema
        movie_info = get_movie_info(tmdb_id)
        genre_ids = [genre.id for genre in movie_info.genres]

        movie = Movie(
            adult=movie_info.adult,
            backdrop_path=movie_info.backdrop_path,
            first_air_date=movie_info.release_date,
            genre_ids=genre_ids,
            id=movie_info.id,
            name=movie_info.title,
            original_language=movie_info.original_language,
            original_name=movie_info.original_title,
            overview=movie_info.overview,
            popularity=movie_info.popularity,
            poster_path=movie_info.poster_path,
            vote_average=movie_info.vote_average,
            vote_count=movie_info.vote_count
        )
        movie_data_list.append(movie)

    response_data = MovieResponse(page=1, results=movie_data_list, total_pages=1, total_results=len(movie_data_list))
    return response_data


def top10NewMovies():
    # db.session.add(new_user_log)
    # db.session.commit()
    sample_movies = [
        Movie(
            backdrop_path="/xGKTgJlqCkq6tAK2sOTdULh7YaX.jpg",
            first_air_date="2022-10-10",
            genre_ids=[10766, 18, 35],
            id=204370,
            name="The Path",
            origin_country=["BR"],
            original_language="pt",
            original_name="Travessia",
            overview="After having her life course changed by a fake image and losing her childhood sweetheart to greed and power, Brisa, a strong woman, will struggle to rebuild her journey, raise her son, rediscover true love, and discover the truth about her origin.",
            popularity=2658.721,
            poster_path="/raDj1xSVzBenwI87arenZY6eHmz.jpg",
            vote_average=4.7,
            vote_count=16
        ),
        Movie(
            backdrop_path=None,
            first_air_date="2005-09-05",
            genre_ids=[18, 35],
            id=36361,
            name="Ulice",
            origin_country=["CZ"],
            original_language="cs",
            original_name="Ulice",
            overview="Ulice is a Czech soap opera produced and broadcast by Nova. In the Czech language Ulice means street.\n\nThe show describes the lives of the Farský, Jordán, Boháč, Nikl, and Liška families and many other people that live in Prague. Their daily battle against real problems of living in a modern world like divorce, love, betrayal and illness or disease. Ulice often shows crime.",
            popularity=2539.81,
            poster_path="/3ayWL13P1HeRnyVL9lU9flOdZjq.jpg",
            vote_average=2.2,
            vote_count=10
        )
    ]

    response_data = MovieResponse(page=1, results=sample_movies, total_pages=1, total_results=len(sample_movies))

    return response_data


def top10PerGenre(genre):
    sample_movies = [
        Movie(
            backdrop_path="/xGKTgJlqCkq6tAK2sOTdULh7YaX.jpg",
            first_air_date="2022-10-10",
            genre_ids=[10766, 18, 35],
            id=204370,
            name="The Path",
            origin_country=["BR"],
            original_language="pt",
            original_name="Travessia",
            overview="After having her life course changed by a fake image and losing her childhood sweetheart to greed and power, Brisa, a strong woman, will struggle to rebuild her journey, raise her son, rediscover true love, and discover the truth about her origin.",
            popularity=2658.721,
            poster_path="/raDj1xSVzBenwI87arenZY6eHmz.jpg",
            vote_average=4.7,
            vote_count=16
        ),
        Movie(
            backdrop_path=None,
            first_air_date="2005-09-05",
            genre_ids=[18, 35],
            id=36361,
            name="Ulice",
            origin_country=["CZ"],
            original_language="cs",
            original_name="Ulice",
            overview="Ulice is a Czech soap opera produced and broadcast by Nova. In the Czech language Ulice means street.\n\nThe show describes the lives of the Farský, Jordán, Boháč, Nikl, and Liška families and many other people that live in Prague. Their daily battle against real problems of living in a modern world like divorce, love, betrayal and illness or disease. Ulice often shows crime.",
            popularity=2539.81,
            poster_path="/3ayWL13P1HeRnyVL9lU9flOdZjq.jpg",
            vote_average=2.2,
            vote_count=10
        )
    ]

    response_data = MovieResponse(page=1, results=sample_movies, total_pages=1, total_results=len(sample_movies))

    return response_data
