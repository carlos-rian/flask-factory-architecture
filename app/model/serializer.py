from flask import Flask
from flask_marshmallow import Marshmallow
from app.model.tables import User

ms = Marshmallow()


def init_app(app: Flask):
    ms.init_app(app=app)


class SerialUser(ms.SQLAlchemyAutoSchema):
    class Meta:
        model = User