from flask import Blueprint, jsonify, session, redirect, abort, send_from_directory, request, current_app
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
    password = request.form.get('password')
    print(password)
    if  password == PASSWORD:
        session["id"] = 1
        return redirect('/')
    else:
        return redirect('/#/login')

@bp.route("/logout")
def logout():
    session.pop("id")
    return redirect('/#/login')

@bp.route("/logged_in")
def logged_in():
    if "id" in session:
        return "ok", 200
    else:
        return "ng", 500
