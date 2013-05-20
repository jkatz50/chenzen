from datetime import datetime
from chenzen.shared.models import db


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    tags = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    published = db.Column(db.DateTime)
    img_url = db.Column(db.String(120))
    author = db.relationship('Users',
                             backref=db.backref('entries', lazy='dynamic'))

    def __init__(self):
        pass
