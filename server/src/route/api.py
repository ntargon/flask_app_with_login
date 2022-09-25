from flask import Blueprint, jsonify, session, redirect, abort, send_from_directory, request, current_app, Response
from functools import wraps
import random

bp = Blueprint('api', __name__, url_prefix='/api')

PASSWORD = 'password' # TODO: 環境変数から読み出す

# api
def login_required(api_method):
    @wraps(api_method)
    def check_api_key(*args, **kwargs):
        if 'id' in session:
            return api_method(*args, **kwargs)
        else:
            abort(401)

    return check_api_key

@bp.route("/rand")
@login_required
def api():
    return str(random.randint(0, 100))

#auth
# TODO: 分割する
@bp.route("/login", methods=['POST'])
def login():
    password = request.get_json().get("password")
    if  password == PASSWORD:
        session["id"] = 1
        return Response(200)
    else:
        return abort(401)

@bp.route("/logout")
def logout():
    if "id" in session:
        session.pop("id")
    return Response(200)

@bp.route("/logged_in")
def logged_in():
    if "id" in session:
        return Response(200)
    else:
        return abort(401)
