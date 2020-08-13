from database.db import db

class Movie(db.Document):
    name = db.StringField(required=True, unique = True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')