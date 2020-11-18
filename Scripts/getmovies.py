from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

target = open("movies.txt", 'w', encoding='utf-8')

collection = db["movies"]
#var = collection.find()

for doc in collection.find():
    print(doc['imdb_rating'],doc['genre'],doc['plot'])
    target.write(doc['imdb_rating'] + "\t")
    target.write(doc['genre'] + "\t")
    target.write(doc['plot'] + "\n")    
