from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel',lazy='dynamic')


    def __init__(self, name):
        self.name = name

    def json(self):
        """Return json format of stores"""

        return { 
            'name': self.name, 
            'items':[item.json() for item in self.items.all()] 
            }
    

    @classmethod
    def find_by_name(cls,name):

        """Find a store filtering by name"""

        return cls.query.filter_by(name=name).first()

    def save_to_db(self):

        """Inserts an store into the database"""

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        """Delete an store from the database"""

        db.session.delete(self)
        db.session.commit()

       
       