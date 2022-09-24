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
export FLASK_CONFIG_FILE_PATH=development.cfg; python server/server.py;
```

**本番時**

```
cd client/; yarn build;
cd ../;
export FLASK_CONFIG_FILE_PATH=production.cfg; python server/server.py;
```
