from flask import Flask, send_from_directory, redirect
import random
from waitress import serve

app = Flask(__name__)
app.config.from_envvar('FLASK_CONFIG_FILE_PATH')
PORT = app.config['PORT']

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

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    if app.config['ENVIRONMENT'] == 'PRODUCTION':
        serve(app, host='0.0.0.0', port=PORT)
    elif app.config['ENVIRONMENT'] == 'DEVELOPMENT':
        app.run(port=5050, debug=True)
    else:
        assert(False)