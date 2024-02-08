from flask import Flask
from service import login, alert

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(login.bp)
app.register_blueprint(alert.bp)
