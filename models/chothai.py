from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin1:admin1@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true"
client= MongoClient(mongo_uri)
db_demo = client.trangchu
db_demo3=client.lienhe
db_demo4=client.tracnghiem
cauhoi=db_demo4['mbti']
dapan_data=db_demo4['dapantracnghiemtc']
lienhe1=db_demo3['lienhe']
db_demo2 = client.moi
cnhn = db_demo["tintuc2"]
tuvan = db_demo2["list"]
# tintuc = cnhn.find()