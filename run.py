#!venv/bin/python
from app import app, socketio, controller
from flask_socketio import SocketIO, send, emit

#ctrl = controller.Controller()
#ctrl.run_monitor_routines()
socketio.run(app, debug=True)
