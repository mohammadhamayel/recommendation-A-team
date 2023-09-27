import numpy as np
from sqlalchemy import text

from recomandationBackEnd import db
from recomandationBackEnd.controller.MovieDbExternalProxy import get_movie_info
from recomandationBackEnd.loaders.logger_config import logger
from recomandationBackEnd.model.MovieResponse import MovieResponse, Movie


def top10RatedMovies():
    engine = db.get_engine()
    query = text("""
            SELECT movieid,title,RatingCount,AvgRating,tmdbId
            FROM top_rated_movies
            WHERE AvgRating > 4
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
                WHERE AvgRating > 3
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
                    WHERE AvgRating > 4
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


def recommendedUserMovies(user_id, data, user_enc, rec_model):
    encoded_user_id = user_enc.transform([user_id])
    seen_movies = set(data[data['userId'] == user_id]['movie'])
    all_movies = set(range(min(data['movie']), max(data['movie']) + 1))
    unseen_movies = list(all_movies - seen_movies)

    model_input = [np.asarray([encoded_user_id[0]] * len(unseen_movies)), np.asarray(unseen_movies)]

    predicted_ratings = rec_model.predict(model_input)
    predicted_ratings = np.max(predicted_ratings, axis=1)
    sorted_index = np.argsort(predicted_ratings)[::-1]

    # number of recomanded movies
    n_movies = 10
    movie_filter = sorted_index[:n_movies].tolist()
    filtered_df = data[data['movie'].isin(movie_filter)]

    recommended_movie_ids = filtered_df['movieId'].unique().tolist()
    logger.info(f'recommended_movie_ids: {recommended_movie_ids}')

    engine = db.get_engine()
    query = text("""
                       select tmdbId from movies where movieId in :movieIdList
                    """)
    with engine.connect() as connection:
        result = connection.execute(query, {'movieIdList': recommended_movie_ids})

    # Create a list to store movie data
    movie_data_list = []

    # Iterate over the query result and create a list of movie data
    for row in result:
        tmdb_id = row[0]
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


def recommendedSimilarMovies(movieName, refined_dataset_nn, knn_similar_movie_model, movie_to_user_df, movies_list,
                             movie_dict, movie_title_id_dict):
    index = movie_dict[movieName]
    knn_input = np.asarray([movie_to_user_df.values[index]])
    n_movies = 10
    n = min(len(movies_list) - 1, n_movies)
    distances, indices = knn_similar_movie_model.kneighbors(knn_input, n_neighbors=n + 1)
    recommended_movie_ids = []
    for i in range(1, len(distances[0])):
        movie_title = movies_list[indices[0][i]]
        movie_id = movie_title_id_dict.get(movie_title)
        if movie_id is not None:
            recommended_movie_ids.append(movie_id)

    logger.info(f'recommended_similar_movie_ids: {recommended_movie_ids}')

    engine = db.get_engine()
    query = text("""
                           select tmdbId from movies where movieId in :movieIdList
                        """)
    with engine.connect() as connection:
        result = connection.execute(query, {'movieIdList': recommended_movie_ids})

    # Create a list to store movie data
    movie_data_list = []

    # Iterate over the query result and create a list of movie data
    for row in result:
        tmdb_id = row[0]
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
