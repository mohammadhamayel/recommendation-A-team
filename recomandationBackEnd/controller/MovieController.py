import numpy as np
from sqlalchemy import text

from recomandationBackEnd import db
from recomandationBackEnd.controller import MovieQueries
from recomandationBackEnd.controller.MovieDbExternalProxy import get_movie_info
from recomandationBackEnd.loaders.logger_config import logger
from recomandationBackEnd.model.MovieExternalInfoModel import MovieExternalModel
from recomandationBackEnd.model.MovieResponse import MovieResponse, Movie


def fetch_movie_data(query, row_index, params=None):
    engine = db.get_engine()

    with engine.connect() as connection:
        if params is None:
            result = connection.execute(text(query))
        else:
            result = connection.execute(text(query).params(**params))

    movie_data_list = []

    for row in result:
        tmdb_id = row[row_index]
        movie_info = get_movie_info(tmdb_id)
        if movie_info is not None and isinstance(movie_info, MovieExternalModel):
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


def top10RatedMovies():
    return fetch_movie_data(MovieQueries.top10RatedMoviesQuery, 4)


def top10NewMovies():
    return fetch_movie_data(MovieQueries.top10NewMoviesQuery, 4)


def top10PerGenre(genre):
    params = {'genre': f'%{genre}%'}
    return fetch_movie_data(MovieQueries.top10PerGenreQuery, 4, params=params)


def recommendedUserMovies(user_id, data, user_enc, rec_model):
    encoded_user_id = user_enc.transform([user_id])
    seen_movies = set(data[data['userId'] == user_id]['movie'])
    all_movies = set(range(min(data['movie']), max(data['movie']) + 1))
    unseen_movies = list(all_movies - seen_movies)

    model_input = [np.asarray([encoded_user_id[0]] * len(unseen_movies)), np.asarray(unseen_movies)]

    predicted_ratings = rec_model.predict(model_input)
    predicted_ratings = np.max(predicted_ratings, axis=1)
    sorted_index = np.argsort(predicted_ratings)[::-1]

    # number of recommended movies
    n_movies = 10
    movie_filter = sorted_index[:n_movies].tolist()
    filtered_df = data[data['movie'].isin(movie_filter)]

    recommended_movie_ids = filtered_df['movieId'].unique().tolist()
    logger.info(f'recommended_movie_ids: {recommended_movie_ids}')
    if len(recommended_movie_ids) == 0:
        return fetch_movie_data(MovieQueries.top10RatedMoviesQuery, 4)

    params = {'movieIdList': recommended_movie_ids}
    return fetch_movie_data(MovieQueries.recommendedUserMoviesQuery, 0, params=params)


def recommendedSimilarMovies(movieId, refined_dataset_nn, knn_similar_movie_model, movie_to_user_df, movies_list,
                             movie_dict):
    logger.info(movie_dict)
    logger.info(movieId)
    if movieId not in movie_dict:
        return MovieResponse(page=1, results=[], total_pages=0, total_results=0)

    index = movie_dict[movieId]
    knn_input = np.asarray([movie_to_user_df.values[index]])
    limit = 10
    n = min(len(movie_dict) - 1, limit)
    distances, indices = knn_similar_movie_model.kneighbors(knn_input, n_neighbors=n + 1)
    recommended_movie_ids = []

    for i in range(1, len(distances[0])):
        movie_id = movies_list[indices[0][i]]
        if movie_id is not None:
            recommended_movie_ids.append(movie_id)

    logger.info(f'recommended_similar_movie_ids: {recommended_movie_ids}')
    if len(recommended_movie_ids) == 0:
        logger.info(f'recommended_similar_movie_ids: {recommended_movie_ids}')
        genre_list = get_genres_by_movie_id(movieId)
        if genre_list:
            params = {'genre': genre_list[0]}
            return fetch_movie_data(MovieQueries.top10PerGenreQuery, 4, params=params)
        else:
            return MovieResponse(page=1, results=[], total_pages=0, total_results=0)

    params = {'movieIdList': recommended_movie_ids}
    return fetch_movie_data(MovieQueries.recommendedSimilarMoviesQuery, 0, params=params)


def get_genres_by_movie_id(movie_id):
    logger.info(f'No recommended_similar_movie_ids--> get_genres_by_movie_id{movie_id}')
    params = {'movieId': movie_id}
    engine = db.get_engine()

    with engine.connect() as connection:
        result = connection.execute(text(MovieQueries.genreByMovieIdMoviesQuery).params(**params))

        genre_list = []

        for row in result:
            genres = row[0]
            genre_list = genres.split('|')

    return genre_list
