from datetime import datetime
from chenzen.shared.models import db


class Users(db.Model):
    username = db.Column(db.String(50), primary_key=True, unique=True)
    password = db.Column(db.String(60))
    created = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.created = datetime.utcnow()
        self.last_login = datetime.utcnow()
