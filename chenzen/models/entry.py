from datetime import datetime
from chenzen import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    tags = db.Column(db.PickleType)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    published = db.Column(db.DateTime)
    img_url = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Entry %r>' % (self.title)
