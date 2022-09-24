from crypt import methods
from operator import methodcaller
from flask import Flask, send_from_directory, redirect, session, request
import random
from waitress import serve

app = Flask(__name__)
app.config.from_envvar('FLASK_CONFIG_FILE_PATH')
app.secret_key = 'hogehoge' # TODO: 環境変数から読み出す
PORT = app.config['PORT']
PASSWORD = 'password' # TODO: 環境変数から読み出す

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory(app.config['SVELTE_MAIN_PAGE_DIR'], 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    if app.config['ENVIRONMENT'] == 'PRODUCTION':
        return send_from_directory(app.config['SVELTE_MAIN_PAGE_DIR'], path)
    elif app.config['ENVIRONMENT'] == 'DEVELOPMENT':
        # viteを使う
        return redirect("http://localhost:5173/" + path)
    else:
        assert(False)

# api
@app.route("/api")
def hello():
    return str(random.randint(0, 100))

@app.route("/login", methods=['POST'])
def login():
    password = request.form.get('password')
    print(password)
    if  password == PASSWORD:
        session["id"] = 1
        return redirect('/')
    else:
        return redirect('/#/login')

@app.route("/logout")
def logout():
    session.pop("id")
    return redirect('/#/login')

@app.route("/logged_in")
def logged_in():
    if "id" in session:
        return "ok", 200
    else:
        return "ng", 500

if __name__ == "__main__":
    if app.config['ENVIRONMENT'] == 'PRODUCTION':
        serve(app, host='0.0.0.0', port=PORT)
    elif app.config['ENVIRONMENT'] == 'DEVELOPMENT':
        app.run(port=5050, debug=True)
    else:
        assert(False)