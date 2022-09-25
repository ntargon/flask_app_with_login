from flask import Blueprint, session, abort, request, Response

bp = Blueprint('auth', __name__, url_prefix='/auth')

PASSWORD = 'password' # TODO: 環境変数から読み出す

#auth
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

