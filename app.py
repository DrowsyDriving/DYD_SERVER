from flask import Flask
from database.connections import DB_URL
from database.model import db
from service import api_login, api_alert

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

db.init_app(app)

app.register_blueprint(api_login.bp)
app.register_blueprint(api_alert.bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)


# app.register_blueprint(login.bp)
# app.register_blueprint(alert.bp)
