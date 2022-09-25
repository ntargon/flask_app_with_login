from flask import Flask
from waitress import serve
import route.root
import route.api
import route.auth

app = Flask(__name__)
app.config.from_envvar('FLASK_CONFIG_FILE_PATH')
app.secret_key = 'hogehoge' # TODO: 環境変数から読み出す
PORT = app.config['PORT']

app.register_blueprint(route.root.bp)
app.register_blueprint(route.api.bp)
app.register_blueprint(route.auth.bp)


if __name__ == "__main__":
    if app.config['ENVIRONMENT'] == 'PRODUCTION':
        serve(app, host='0.0.0.0', port=PORT)
    elif app.config['ENVIRONMENT'] == 'DEVELOPMENT':
        app.run(port=5050, debug=True)
    else:
        assert(False)