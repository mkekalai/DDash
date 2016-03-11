from app import db

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), index=True)
    httpstatus = db.Column(db.Integer)
    queryresults = db.relationship('Status', backref='author', lazy='dynamic')

    def __init__(self, url=None, httpstatus=None):
        self.url = url
        self.httpstatus = httpstatus
    
    def __repr__(self):
        return 'Resource(%r,%r)' % (self.url, self.httpstatus)

''' History record of status change '''
class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    httpstatus = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))

    def __init__(self, httpstatus=None, timestamp=None, resource_id=None):
        self.httpstatus = httpstatus
        self.timestamp = timestamp
        self.resource_id = resource_id

    def __repr__(self):
        return 'Status(%r,%r)' % (self.httpstatus, self.timestamp)
