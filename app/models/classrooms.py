from ..extensions import db

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(50))
    room_number = db.Column(db.String(50))