import joblib
from flask import request, jsonify

from recomandationBackEnd.loaders.data_loader import load_data
from recomandationBackEnd.loaders.encoders import encode_data
from recomandationBackEnd.loaders.logger_config import log_request_response_details
from recomandationBackEnd import create_app
from recomandationBackEnd.loaders.model_loader import load_recommendation_model, load_similar_model
from recomandationBackEnd.loaders.similar_prepare import prepare_knn

from recomandationBackEnd.view import MovieView
from recomandationBackEnd.view import UserLogView

app = create_app()

# Initialize variables to hold model and data
refined_dataset_nn = None
rec_model = None
user_enc = None
item_enc = None
knn_similar_movie_model = None
movie_to_user_df = None
movies_list = None
movie_dict = None


def before_first_request():
    global refined_dataset_nn, rec_model, user_enc, item_enc, knn_similar_movie_model, \
        movie_to_user_df, movies_list, movie_dict

    try:
        # Load CSV data into a Pandas DataFrame
        data_path = "F:/DataScience/AncaondaWorkspace/GZG/FinalProjectRecommanded/refined_dataset_nn.csv"
        refined_dataset_nn = load_data(data_path)

        # Load the recommendation model (load it only once)
        model_path = './mlmodel/MovieRecomendationModel.h5'
        rec_model = load_recommendation_model(model_path)

        # Encode user and item
        refined_dataset_nn, user_enc, item_enc = encode_data(refined_dataset_nn, 'userId', 'title', 'rating')

        # Load Similar Model
        similar_model_path = './mlmodel/similarmovie_recommendation_model2.pkl'
        knn_similar_movie_model = load_similar_model(similar_model_path)
        movie_to_user_df, movies_list, movie_dict = prepare_knn(refined_dataset_nn)

    except Exception as e:
        app.logger.error(f"Error during model and data initialization: {str(e)}")


# Global error handler for all exceptions
@app.errorhandler(Exception)
def handle_global_error(error):
    app.logger.error(f'Global error handler caught an exception: {str(error)}')

    error_message = 'An error occurred while processing request.'
    status_code = 500

    if isinstance(error, ValueError):
        error_message = 'Invalid input. Please check  data.'

    response = jsonify({'error': error_message})
    response.status_code = status_code

    return response


@app.route('/api/userLog/add', methods=['POST'])
def add_user_log():
    try:
        log_request_response_details(request)
        response = UserLogView.add_user_log(request)
        log_request_response_details(response)
        return response
    except Exception as e:
        raise e


@app.route('/api/userLog/get/<int:logId>', methods=['GET'])
def get_user_log(logId):
    try:
        log_request_response_details(request)
        response = UserLogView.get_user_log(logId)
        log_request_response_details(response)
        return response
    except Exception as e:
        raise e


@app.route('/api/recommendation/perUser/<int:userId>', methods=['GET'])
def recommended_per_user(userId):
    try:
        log_request_response_details(request)
        response = MovieView.recommendedUserMovies(userId, refined_dataset_nn, user_enc, rec_model)
        log_request_response_details(response)
        return response
    except Exception as e:
        raise e


@app.route('/api/recommendation/perMovie/<int:movieId>', methods=['GET'])
def recommended_per_movie(movieId):
    try:
        log_request_response_details(request)
        response = MovieView.recommendedSimilarMovies(movieId, refined_dataset_nn, knn_similar_movie_model,
                                                      movie_to_user_df, movies_list, movie_dict)
        log_request_response_details(response)
        return response
    except Exception as e:
        raise e


@app.route('/api/movies/top10RatedMovies', methods=['GET'])
def top10RatedMovies():
    try:
        log_request_response_details(request)
        response = MovieView.top10RatedMovies()
        log_request_response_details(response)
        return response
    except Exception as e:
        raise e


@app.route('/api/movies/top10NewMovies', methods=['GET'])
def top10NewMovies():
    try:
        log_request_response_details(request)
        response = MovieView.top10NewMovies()
        log_request_response_details(response)
        return response
    except Exception as e:
        raise e


@app.route('/api/movies/top10PerGenre/<string:genre>', methods=['GET'])
def top10PerGenre(genre):
    try:
        log_request_response_details(request)
        response = MovieView.top10PerGenre(genre)
        log_request_response_details(response)
        return response
    except Exception as e:
        raise e


if __name__ == '__main__':
    before_first_request()
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
