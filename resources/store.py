from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self,name):
        """get a store from database"""
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        return {'message':'Store does not exixts'},404

    
    def post(self,name):
        """save a store to database"""
        if StoreModel.find_by_name(name):
            return {
                'message':f'A store with name {name} already exits'
                },400
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {
                'message':'An error occurred while creating a store.'
            },500
        
        return store.json(),201

    def delete(self,name):
        """delete a store from database"""
        store = StoreModel.find_by_name(name)
        
        if store:
            store.delete_from_db()

        return {'message':'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {
            'stores':[store.json() for store in StoreModel.query.all()]
            }
