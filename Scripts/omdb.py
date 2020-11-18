import pymongo
from omdb import OMDBClient

API_KEY = "1be59909"
client = OMDBClient(apikey=API_KEY)
search_key = ["canada", "university", "moncton", "halifax", "toronto", "vancouver", "alberta", "niagara"]
searched = []
searchfull = []

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["movies"]

for item in search_key:
    searched = client.search(item)
    for data in searched:
        details = client.imdbid(data["imdb_id"])
        genre = details['genre']
        imdb_rating = details['imdb_rating']
        plot = details['plot']
        imdb_id = details['imdb_id']
        title = details['title']
        year = details['year']
        type = details['type']
        searchfull.append({'imd_bid': imdb_id, 'title': title, 'year': year, 'type': type,
                           'genre': genre, 'imdb_rating': imdb_rating, 'plot': plot})
x = mycol.insert_many(searchfull)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)
