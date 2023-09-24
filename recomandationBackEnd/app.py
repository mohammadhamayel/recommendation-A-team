from flask import request
from recomandationBackEnd import create_app
from recomandationBackEnd.view import UserLogView
from recomandationBackEnd.view import MovieView
 
app = create_app()


# Define routes for CRUD operations
@app.route('/api/userLog/add', methods=['POST'])
def add_user_log():
    return UserLogView.add_user_log(request)


@app.route('/api/userLog/get/<int:logId>', methods=['GET'])
def get_user_log(logId):
    return UserLogView.get_user_log(logId)


@app.route('/api/recommendation/perUser/<int:logId>', methods=['GET'])
def recommended_per_user(logId):
    return UserLogView.get_user_log(logId)


@app.route('/api/recommendation/perMovie/<int:logId>', methods=['GET'])
def recommended_per_movie(logId):
    return UserLogView.get_user_log(logId)


@app.route('/api/movies/top10RatedMovies', methods=['GET'])
def top10RatedMovies():
    return MovieView.top10RatedMovies()

@app.route('/api/movies/top10NewMovies', methods=['GET'])
def top10NewMovies():
    return MovieView.top10NewMovies()

@app.route('/api/movies/top10PerGenre/<string:genre>', methods=['GET'])
def top10PerGenre(genre):
    return MovieView.top10PerGenre(genre)

@app.route('/api/movies/combinedTop10', methods=['GET'])
def combinedTop10():
    return MovieView.top10NewMovies()

if __name__ == '__main__':
    app.run(debug=True)
