# Users Model
from .db import db


class User(db.Document):
    name = db.StringField(max_length=30, required=True, unique=False)
    email = db.StringField(max_length=30, required=True, unique=True)
    password = db.StringField(max_length=200, required=True)

