from recomandationBackEnd import db
from recomandationBackEnd.model.UserLogModel import UserLog
from recomandationBackEnd.schema.ResponseSchema import create_response


def add_user_log(userId, actionEvent, movieId, rating, recommendedMovies):
    new_user_log = UserLog(
        userId=userId,
        actionEvent=actionEvent,
        movieId=movieId,
        rating=rating,
        recommendedMovies=recommendedMovies
    )
    db.session.add(new_user_log)
    db.session.commit()
    return create_response(0, 'User log entry added successfully')


def get_user_log(userId):
    return UserLog.query.filter(UserLog.userId == userId).all()
