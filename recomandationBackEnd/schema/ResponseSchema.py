from marshmallow import Schema, fields


class ResponseSchema(Schema):
    code = fields.Int(required=True)
    message = fields.String(required=True)
    data = fields.Dict()


def create_response(code, message, data=None):
    response_data = {
        'code': code,
        'message': message,
    }
    if data is not None:
        response_data['data'] = data
    return response_data
