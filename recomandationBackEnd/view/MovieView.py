from flask import jsonify

from recomandationBackEnd.controller import MovieController
from recomandationBackEnd.schema.MovieSchema import MovieResponseSchema


def top10RatedMovies():
    movies = MovieController.top10RatedMovies()

    if movies:
        movie_response_schema = MovieResponseSchema()
        serialized_result = movie_response_schema.dump(movies)
        return jsonify(serialized_result), 200
    else:
        return jsonify({'message': 'No Movies found'}), 404


def top10NewMovies():
    movies = MovieController.top10NewMovies()
    if movies:
        #movie_schema = MovieSchema(many=True)
        movie_response_schema = MovieResponseSchema()
        #serialized_movies = movie_schema.dump(movies.results)
        serialized_response = movie_response_schema.dump(movies)
        # response_json = {
        #     'page': movies.page,
        #     'results': serialized_movies,
        #     'total_pages': movies.total_pages,
        #     'total_results': movies.total_results,
        # }

        return jsonify(serialized_response), 200
    else:
        return jsonify({'message': 'No Movies found'}), 404

def top10PerGenre(genre):
    movies = MovieController.top10PerGenre(genre)
    if movies:
        movie_response_schema = MovieResponseSchema()
        serialized_result = movie_response_schema.dump(movies)
        return jsonify(serialized_result), 200
    else:
        return jsonify({'message': 'No Movies found'}), 404
