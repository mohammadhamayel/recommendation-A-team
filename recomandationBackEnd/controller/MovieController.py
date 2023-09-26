from sqlalchemy import text

from recomandationBackEnd import db
from recomandationBackEnd.controller.MovieDbExternalProxy import get_movie_info
from recomandationBackEnd.model.MovieResponse import MovieResponse, Movie


def top10RatedMovies():
    engine = db.get_engine()
    query = text("""
            SELECT movieid,title,rating,RatingCount,AvgRating,tmdbId
            FROM top_rated_movies
            WHERE Rating > 4
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
            release_date=movie_info.release_date,
            genre_ids=genre_ids,
            id=movie_info.id,
            title=movie_info.title,
            original_language=movie_info.original_language,
            original_title=movie_info.original_title,
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
    engine = db.get_engine()
    query = text("""
                SELECT movieid,RatingCount,AvgRating,release_date,tmdbId
                FROM top_rated_movies
                WHERE Rating > 3
                AND release_date >= '2019-01-01'
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
            release_date=movie_info.release_date,
            genre_ids=genre_ids,
            id=movie_info.id,
            title=movie_info.title,
            original_language=movie_info.original_language,
            original_title=movie_info.original_title,
            overview=movie_info.overview,
            popularity=movie_info.popularity,
            poster_path=movie_info.poster_path,
            vote_average=movie_info.vote_average,
            vote_count=movie_info.vote_count
        )
        movie_data_list.append(movie)

    response_data = MovieResponse(page=1, results=movie_data_list, total_pages=1, total_results=len(movie_data_list))
    return response_data


def top10PerGenre(genre):
    engine = db.get_engine()
    query = text("""
                    SELECT  MovieID,Title,RatingCount,AvgRating ,tmdbId
                    FROM top_rated_movies
                    WHERE Rating > 4
                    and genres like :genre
                    ORDER BY RatingCount DESC
                    LIMIT 10;
                """)
    with engine.connect() as connection:
        result = connection.execute(query, {'genre': f'%{genre}%'})

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
            release_date=movie_info.release_date,
            genre_ids=genre_ids,
            id=movie_info.id,
            title=movie_info.title,
            original_language=movie_info.original_language,
            original_title=movie_info.original_title,
            overview=movie_info.overview,
            popularity=movie_info.popularity,
            poster_path=movie_info.poster_path,
            vote_average=movie_info.vote_average,
            vote_count=movie_info.vote_count
        )
        movie_data_list.append(movie)

    response_data = MovieResponse(page=1, results=movie_data_list, total_pages=1, total_results=len(movie_data_list))
    return response_data

