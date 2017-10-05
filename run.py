from app import app
from db import db

# this is to solve the error for db not found

db.init_app(app)

# create db before all request is run
@app.before_first_request
def create_tables():
	db.create_all()
