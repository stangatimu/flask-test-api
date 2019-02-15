from flask_restful import reqparse,Resource
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help = "This filed cannot be left blank"
    )

    parser.add_argument('store_id',
            type=int,
            required=True,
            help = "Every item needs a store id"
    )
    
    @jwt_required()
    def get(self,name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {"message":"Errors occurred search for item"}, 500

        if item:
            return item.json(),200 
        return {'message':'item not found'},404

           

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'name':f'An item with name {name} already exists'},400        

        data = Item.parser.parse_args() #pass force=True silent=True
        item = ItemModel(name,data['price'],data['store_id'])

        try:
            item.save_to_db()
        except:
            return {"message":f"An error occurred saving {name}"},500


        return item.json(), 201

    def delete(self,name):
        item = ItemModel.find_by_name(name)

        if item:
           item.delete_from_db()
        
        return {'message':'item has been deleted'},200

    def put(self,name):
        
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
           item.price = data['price']
           item.store_id = data['store_id']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json(),201

class ItemList(Resource):
    def get(self):
        return {
            'items':[item.json() for item in ItemModel.query.all()]
            # 'items':list(map(lambda x: x.json(),ItemModel.query.all()))
            }, 200