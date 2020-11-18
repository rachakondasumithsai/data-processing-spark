import re
import sys
import time
import pymongo
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("stOGyiJB2YiiOseFkCrC1Xy6f",
                       "2IB7FYAYMHe7W0vUZ5EvAqhOQkPhFOhzucVr2tPrOYEl0oiq6y")
auth.set_access_token("201589155-7nOHwAEWkpk8B56UT2wX1cW04Ze0lbHa0Sc4bL1M",
                      "HMg5XO4K8Hg1U0ivohb6fw67mluVq3mMhcSs4aUlwHnvs")

api = tweepy.API(auth, wait_on_rate_limit=True,
             wait_on_rate_limit_notify=True)


def clean_tweet(tweet):
    """
    Utility function to close tweet text by removing links,
    special charecters
    using simple regex statements.
    """
    return (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|\
                             (\w+:\/\/\S+)",
                            " ", tweet).split()))


search_words = ["Canada", "University", "Dalhousie University", "Canada Education", "Halifax"]
#date_since = "2010-11-16"
target = open("mytweets.txt", 'w', encoding='utf-8')

# Collect tweets
 
tweet_to_store = []
count = 1
count1=1
try:
    for items in search_words:
        print('Searching for keyword: ' + items)
        tweets = tweepy.Cursor(api.search,
                       q=items,
                       lang="en",
                       result_type="recent").items(400)
        for tweet in tweets:
            tweet_text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|\
                             (\w+:\/\/\S+)",
                            " ", tweet.text)
            target.write(tweet_text + "\n")
            tweet_user = tweet.user.screen_name
#       tweet_location = tweet.loc
            tweet_id = tweet.id
            retweet_count = tweet.retweet_count
            favorite_count = tweet.favorite_count
            retweeted = tweet.retweeted
            created_at = tweet.created_at

            tweet_to_store.append(
                    {'tweet_text': tweet_text, 'tweet_user': tweet_user,
                     'tweet_likes': favorite_count, 'tweet_id': tweet_id, 'retweet_count': retweet_count,
                     'is_retweeted': retweeted, 'created_at': created_at})
    
except tweepy.RateLimitError:
                    for i in range(2 * 60, 0, -1):
                        time.sleep(1)
                        sys.stdout.write("\r")
                        sys.stdout.write("{:2d} seconds remaining.".format(i))
                        sys.stdout.flush()
                        continue
except Exception as e:
            print('Tweets read: ' + str(len(tweet_to_store)))
            print(e)
#except tweepy.TweepError as e:
#                    print(e)
#                    exit()
#except Exception as e:
#                    print(e)
#                    exit()
#except tweepy.error as e:
#                    print(e)
#                    exit()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["tweets"]

x = mycol.insert_many(tweet_to_store)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
 