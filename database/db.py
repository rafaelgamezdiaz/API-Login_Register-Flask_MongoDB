# Initializing Database
from flask_mongoengine import MongoEngine

# Creating db object
db = MongoEngine()

# Host
host = 'mongodb://localhost/database_mdb'


# Initialize Database
def initialize_db(app):
    db.init_app(app)
