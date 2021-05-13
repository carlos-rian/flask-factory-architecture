from flask import Flask, request
from app.controller.user import select_user
from app.controller.user import create_user
from app.controller.user import update_user
from app.controller.user import delete_user

# o flask está importado apenas para indicar que o app é do tipo flask.
def init_app(app: Flask):
    @app.route("/user/<username>", methods=["GET"])
    def get_user(username):
        return select_user(username=username)

    @app.route("/user", methods=["POST"])
    def post_user():
        data = request.json
        if not data:
            return {"message": "Ops, error user not missing."}, 400
        return create_user(data=data)

    @app.route("/user/<username>", methods=["PUT"])
    def change_user(username):
        data = request.json
        if not data:
            return {"message": "Ops, error user not missing."}, 400
        return update_user(data=data, username=username)

    @app.route("/user/<username>", methods=["DELETE"])
    def drop_user(username):
        return delete_user(username=username)

    @app.route("/")
    def home():
        body = {
            "username": "xpto",
            "password": "12345",
            "name": "carlos silva",
            "email": "xpto@gmail.com",
        }
        routes = {
            "get": {"route": "/user/<username>", "path": "Pedrinho"},
            "post": {"route": "/user", "body": body},
            "put": {"route": "/user/<username>", "path": "Pedrinho", "body": body},
            "delete": {"route": "/user/<username>", "path": "Pedrinho"},
        }
        return {"routes": routes}