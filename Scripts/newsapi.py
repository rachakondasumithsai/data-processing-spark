# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:39:36 2020

@author: racha
"""

import pymongo 
import requests
import json
import re

#api = NewsApiClient(api_key='92c12525ca5f4ed5a6f26f4b36d23d4a')
api_key='92c12525ca5f4ed5a6f26f4b36d23d4a'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["news"]


searchnews=[]
searchfullnews=[]
searchkeynews=["Canada", "University", "Dalhousie University", "Canada Education", "Halifax","Moncton","Toronto"]

for item in searchkeynews:
                for pg in range(1, 2):
                    response = requests.get("https://newsapi.org/v2/everything",
                                       {'q': item, 'language': 'en',
                                        'sortBy': 'popularity', 'apiKey': '92c12525ca5f4ed5a6f26f4b36d23d4a',
                                        'pageSize':  100, 'page': pg})
                    response_json = json.loads(response.text)
                    print(response_json)
                    for article in response_json['articles']:
                        if article.get('description') is None or article.get('content') is None:
                            continue
                        article_author = article['author']
                        article_title = article['title']
                        article_description = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|\
                             (\w+:\/\/\S+)",
                            " ", article.get('description',''))
                        if article.get('description') is None:
                            continue
                        else:
                            article_content = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|\
                             (\w+:\/\/\S+)",
                            " ", article.get('content',''))
                        article_timestamp = article['publishedAt']
                        searchfullnews.append({'article_author': article_author, 'article_title': article_title, 'article_description': article_description, 'article_content': article_content, 'article_timestamp': article_timestamp})
 
mycol.insert_many(searchfullnews)