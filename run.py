#!venv/bin/python
from app import app, socketio, controller
from flask_socketio import SocketIO, send, emit

socketio.run(app, debug=True)
