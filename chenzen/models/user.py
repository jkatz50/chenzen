from datetime import datetime
from chenzen import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(60))
    created = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    entries = db.relationship('Entry', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)
