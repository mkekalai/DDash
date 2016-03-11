from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app)
db = SQLAlchemy(app)

from app import views, models
