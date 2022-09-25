# ログイン機能を備えたflaskアプリのテスト


本番時は`waitress`を使う


実行方法

**開発時**

at terminal 1
```
cd client/; yarn vite; # terminal 1
```
at terminal 2
```
cd server/src/;
export FLASK_CONFIG_FILE_PATH=../development.cfg; python app.py;
```

**本番時**

at terminal 1
```
cd client/; yarn build;
```
at terminal 2
```
cd server/src/;
export FLASK_CONFIG_FILE_PATH=../production.cfg; python app.py;
```
