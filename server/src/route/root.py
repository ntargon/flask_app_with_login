from flask import Blueprint, jsonify, session, redirect, abort, send_from_directory, request, current_app
from functools import wraps

bp = Blueprint('root', __name__, url_prefix='/')

# Path for our main Svelte page
@bp.route("/")
def base():
    return send_from_directory(current_app.config['SVELTE_MAIN_PAGE_DIR'], 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@bp.route("/<path:path>")
def home(path):
    if current_app.config['ENVIRONMENT'] == 'PRODUCTION':
        return send_from_directory(current_app.config['SVELTE_MAIN_PAGE_DIR'], path)
    elif current_app.config['ENVIRONMENT'] == 'DEVELOPMENT':
        # viteを使う
        return redirect("http://localhost:5173/" + path)
    else:
        assert(False)
