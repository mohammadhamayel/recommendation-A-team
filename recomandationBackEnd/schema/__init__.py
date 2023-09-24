from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from recomandationBackEnd.model.UserLogModel import UserLog


class UserLogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserLog


class UserLogRequestSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserLog
        exclude = ('logId', 'eventTime')
