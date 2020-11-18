# data-processing-spark

## A. Cluster Setup
1. I have created the cloud account in AWS. I have created an EC2 instance of ubuntu version. Please see the image aws_screenshot.pnf
2. I have initialized Apache spark in my cloud account. Please see image apachespark.png
4. Installation of mongoDB is done in cloud. Please the screenshot mongoinstall.png
## B. Twitter data extraction and transformation
5. Created a twitter developer account. Please see image twitterdeveloper.png
6. Explored tweepy API.
I have installed tweepy package. I have used this package in twitterapi.py file and authenticated myself with all the tockens. Then I have retrieved the data using Cursor method and search method in this API. It returned a JSON structure. I have considered only few keys such as text, user, likes, time etc. I have extracted all the data using loops. I have cleaned the text by using regular expression technique and re package available inbuilt with python.
7. I have considered only search terms Canada, University, Dalhousie University, Canada education, Halifax.
8. I have also written the tweets into a text file named mytweets.txt. I have stored all the data from tweets as key-value pairs in a list. Later I have uploaded this list to my mongoDB server using pymongo package. Please see the screenshot tweetsdatabase.png. The script file is temp.py. All tweets ae saved into mytweets.txt.
### News article data exraction & transformation
9. Explored https://newsapi.org/
10. I have requested API key through their website. Please see screenshot newsapiaccount.png
11. I have installed newsapi for python package. I have selected only "Canada", "University", "Dalhousie University", "Canada Education", "Halifax", "Moncton", "Toronto" keywords for searching of news. I have used requests.get() method to get a response from the API by using my key. I got a response as json fromat.
12. I have cleaned this response by using regular expressions technique by re package.
13. I have uploaded the extracted and cleaned data into mongoDB using pymongo package. Please see the screenshot newsdatabase.png. The script file is newsapi.py.
### Movie data extraction and transformation
14. Explored http://www.omdbapi.com/
15. I have requested API key through their website. Please see the screenshot omdbdeveloper.png.
16. I have installed omdb package and used OMDBClient and my api key I have connected to the API. I have only selected "canada", "university", "moncton", "halifax", "toronto", "vancouver", "alberta", "niagara" to search the films. I have used client.search() method to search data of films which has the above keywords. I have considered only id, title, year, type for getting data.
17. After getting the data I have cleaned it using regular expressions technique by re package.
18. I have uploaded the extracted and cleaned data into MongoDB using pymongo package. Please see the screenshot moviesdatabase.png. The script file is omdb.py

## C. Data processing (Spark)
19. I have installed spark framework in cloud server using some commands. Please see screenshot apachespark.png. I have also installed python. I have installed pyspark package which acts as a connector between spark and python. I have also set the environment variables so that in future there will be no problem when I use spark framework. I have opened spark shell and entered the code over the shell. The code is present in wordcountnew.py and I have saved it into text file also named count.txt. Please see the screenshots wordcount1.png, wordcount2.png, wordcount3.png, wordcount4.png.
I have used pyspark and mongodb to connect the database and retrieved the collections and performed count operation and displayed the results. The script file is wordcountnew.py
20. I have used pymongo and got the movies collection from database. I have only printed Genre, Plot, Ratings in console and text file named movies.txt. The scriptfile is getmovies.py
## References
* [1] “OMDb API - The Open Movie Database,” www.omdbapi.com. [Online]. Available:
http://www.omdbapi.com/. [Accessed: 27-Mar-2020].
* [2] D. Gilland, “omdb: Python wrapper for OMDb API: http://www.omdbapi.com/,” PyPI. [Online]. Available: https://pypi.org/project/omdb. [Accessed: 27-Mar-2020].
* [3] “Tweepy Documentation — tweepy 3.8.0 documentation,” docs.tweepy.org. [Online]. Available:
http://docs.tweepy.org/en/latest/. [Accessed: 27-Mar-2020].
* [4] “MongoDB Documentation,” docs.mongodb.com. [Online]. Available: https://docs.mongodb.com/.
[Accessed: 27-Mar-2020].
* [5] “Welcome: Documentation for newsapi-python — newsapi-python 0.2.6 documentation,” newsapi-
python.readthedocs.io. [Online]. Available: https://newsapi-python.readthedocs.io/en/latest/. [Accessed: 2-Mar-2020].
* [6] “PyMongo 3.9.0 Documentation — PyMongo 3.9.0 documentation,” Mongodb.com, 2019. [Online].
Available: https://api.mongodb.com/python/current/. [Accessed: 27-Mar-2020].
* [7] M. Papiernik, “How to Install MongoDB on Ubuntu 18.04,” DigitalOcean, 07-Jun-2018. [Online]. Available: https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-18-04. [Accessed: 27-Mar-2020].
* [8] “Welcome to Spark Python API Docs! — PySpark 2.4.5 documentation,” spark.apache.org. [Online].
Available: https://spark.apache.org/docs/latest/api/python/index.html. [Accessed: 27-Mar-2020].