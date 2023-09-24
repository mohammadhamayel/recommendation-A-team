from flask import jsonify, json
from marshmallow import ValidationError
from recomandationBackEnd.schema import UserLogRequestSchema, UserLogSchema
from recomandationBackEnd.controller import UserLogController
from recomandationBackEnd.schema.ResponseSchema import ResponseSchema


def add_user_log(request):
    try:
        data = request.get_json()

        response = UserLogController.add_user_log(
            data['userId'],
            data['actionEvent'],
            data['movieId'],
            data['rating'],
            data['recommendedMovies']
        )
        # Serialize the response using UserLogSchema
        response_schema = ResponseSchema()
        serialized_result = response_schema.dump(response)

        return jsonify(serialized_result), 201

    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def get_user_log(logId):
    user_log = UserLogController.get_user_log(logId)
    if user_log:
        user_log_schema = UserLogSchema(many=True)
        serialized_result = user_log_schema.dump(user_log)
        return jsonify(serialized_result), 200
    else:
        return jsonify({'message': 'User log not found'}), 404
