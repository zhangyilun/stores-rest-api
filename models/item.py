from db import db


class ItemModel(db.Model):

	# tell sqlalchemy db and column information
	__tablename__ = "items"
	id = db.Column(db.Integer, primary_key=True) # good to always have the id
	name = db.Column(db.String(80)) # with some limitations
	price = db.Column(db.Float(precision=2)) # with some limitations

	store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
	store = db.relationship("StoreModel")
	# find store in database to match store_id

	def __init__(self, name, price, store_id):
		self.name = name
		self.price = price
		self.store_id = store_id


	def json(self):
		return {"name": self.name, "price": self.price}


	@classmethod
	def find_by_name(cls, name):
		# .query is from the db.Model class
		# the same as "SELECT * FROM items WHERE name=name LIMIT 1"
		return cls.query.filter_by(name=name).first()


	# this will do both insert and update
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()


	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()

