from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from tensorflow import keras

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost:3306/movielensdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy and Marshmallow with the app
    db.init_app(app)
    ma.init_app(app)


    return app
