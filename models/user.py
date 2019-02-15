import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_to_db(self):
        """Save a user to the database"""
        db.session.add(self)
        db.session.commit()
            
    @classmethod
    def find_by_username(cls,username):
         
        """Gets a user by username from database"""

        return cls.query.filter_by(username=username).first()        

    @classmethod
    def find_by_id(cls,_id):
         
        """Gets a user by id from database"""

        return cls.query.filter_by(id=_id).first()
