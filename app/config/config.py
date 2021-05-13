from os import getenv
from flask import Flask


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///database.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False