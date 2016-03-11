import httplib, datetime, time
from app import models, db
from thread import start_new_thread
from flask_socketio import emit
import logging

logging.basicConfig()

class Controller():
    
    # Routine for polling status codes for resources
    def update_all_statuses(self):
        resources = models.Resource.query.all()
        changes_occurred = False
        for r in resources:
            try:
                conn = httplib.HTTPConnection(r.url)
                conn.request('GET','/')
                resp = conn.getresponse().status
            except:
                resp = 404
            # Save only changes to status table
            if int(resp) != int(r.httpstatus):
                changes_occurred = True
                r.httpstatus = resp
                dt = datetime.datetime.now()
                status = models.Status(r.httpstatus, dt, r.id )
                db.session.add(r)
                db.session.add(status)
                db.session.commit()
        return changes_occurred
                        
    def get_status(self, url):
        try:
            conn = httplib.HTTPConnection(url)
            conn.request('GET','/')
            return conn.getresponse().status
        except:
            return 404
