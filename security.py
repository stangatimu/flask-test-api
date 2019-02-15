from werkzeug.security import safe_str_cmp

from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)

    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']

    return UserModel.find_by_id(user_id)

# users = [
#     User(1,'stan','1234')     
# ]
# username_mapping = {u.username: u for u in users}
# username_mapping = {
#     'stan':{
#         'id':1,
#         'username':'stan',
#         'password':'1234'        
#     }
# }
# userid_mapping ={u.id: u for u in users}
# userid_mapping ={
#     'id':{
#         'id':1,
#         'username':'stan',
#         'password':'1234'
#     }
# }