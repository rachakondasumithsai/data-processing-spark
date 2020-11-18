# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 01:59:22 2020

@author: racha
"""

from pymongo import MongoClient
import pyspark

client = MongoClient("mongodb://localhost:27017/")
mycol = client["mydatabase"]

target = open("count.txt", 'w', encoding='utf-8')

#sc = pyspark.SparkContext('local[*]')
sc = pyspark.SparkContext.getOrCreate('local[*]')

tweets = mycol["tweets"]
count = 0
tweettext = ""
for data in tweets.find():
    tweettext += data["tweet_text"].lower()
    tweettext += " "
    count += 1
print("total tweets")
print(count)

count = 0
news = mycol["news"]
newstext = ""
for data in news.find():
    newstext += data["article_description"].lower()
    newstext += " "
    count += 1
print("total news")
print(count)

alltext = tweettext + "\n" + newstext
words = sc.parallelize([alltext]).flatMap(lambda line: line.split(" "))
countwords = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
#sortedwords = sorted(countwords, key=lambda arg: arg.lower())
sortedwords = countwords.sortBy(lambda x: x[1], False)

#sortedwords = countwords.sortBy(lambda x: x[1], False)
for word, count in sortedwords.toLocalIterator():
            if word in ["education", "canada", "university", "dalhousie", "expensive", "good school", "faculty", "computer",
                        "science", "schools", "school", "good", "bad", "poor", "graduate"]:
               target.write(f"{word}: {count} \n")
               print(f"{word} : {count}")

