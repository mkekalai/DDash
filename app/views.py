from flask import render_template, request, copy_current_request_context
from app import app, models, controller, socketio, db
from flask_socketio import emit, send
from apscheduler.schedulers.background import BackgroundScheduler
import time

ctrl = controller.Controller()

# Starts interval for httpstatus updates
@app.before_first_request
def initialize():

        @copy_current_request_context
        def process_status_updates():
                # Send new data to client if data has status changes
                update_client = ctrl.update_all_statuses()
                if(update_client):
                        items = models.Resource.query.all()
                        socketio.send(render_template('new_items.html',
                                                      items=items) )
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(process_status_updates, 'interval', seconds=30)

@app.route('/')
@app.route('/index')
def index():
        items = models.Resource.query.all()
        return render_template('dashboard.html',
                               title='Home',
                               items=items)

@app.route('/new-resource', methods=['GET','POST'])
def newresource():
        url = request.form['url']
        status = ctrl.get_status(url)
        new_resource = models.Resource(url,status)
        db.session.add(new_resource)
        db.session.commit()
        socketio.emit('new_item',
                      render_template('new_item.html', item=new_resource),
                      broadcast=True)

# Remove item from database and emit remove permission to client
@socketio.on('remove_item')
def remove_item(json):
        removable_resource = models.Resource.query.filter(models.Resource.id == json['item_id']).first()
        db.session.delete(removable_resource)
        db.session.commit()        
        emit('remove_ui_item', { 'id' : json['item_id'] })
