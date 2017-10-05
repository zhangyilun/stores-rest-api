from app import app
from db import db

# this is to solve the error for db not found

db.init_app(app)
