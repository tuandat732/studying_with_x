from pymongo import MongoClient

mongo_uri = 'mongodb+srv://admin1:admin1@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true'

client = MongoClient(mongo_uri)

database_user = client.data_user

user = database_user['account']

# new_user = {
#     'username':'quocthai200x',
#     'password':'Thai123456',
#     'hoa':[],
#     'li':[],
#     'sinh':[],
#     'toan':[],
#     'anh':[]
# }

# user.insert_one(new_user)