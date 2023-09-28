from sqlalchemy import func
from recomandationBackEnd import db


class UserLog(db.Model):
    __tablename__ = 'user_logs'

    logId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=True)
    actionEvent = db.Column(db.String(255), nullable=True)
    movieId = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.String(255), nullable=True)
    recommendedMovies = db.Column(db.String(255), nullable=True)
    eventTime = db.Column(db.TIMESTAMP, nullable=False, default=func.current_timestamp())

    def __init__(self, userId, actionEvent, movieId, rating, recommendedMovies):
        self.userId = userId
        self.actionEvent = actionEvent
        self.movieId = movieId
        self.rating = rating
        self.recommendedMovies = recommendedMovies
