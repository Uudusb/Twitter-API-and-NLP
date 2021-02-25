import tweepy
from textblob import TextBlob
import preprocessor
import statistics
from typing import List
import preprocessor as p
import statistics

from secrets import comsumerKey, consumerSecret

auth = tweepy.AppAuthHandler(consumer_key=comsumerKey, consumer_secret=consumerSecret)
api = tweepy.API(auth)

def getTweets(keyword: str) -> List[str]:
    allTweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(30):
        allTweets.append(tweet.full_text)
    return allTweets

def cleanTweets(allTweets: List[str]) -> List[str]:
    tweetsClean = []
    for tweet in allTweets:
        tweetsClean.append(p.clean(tweet))
    return tweetsClean

def getSentiment(allTweets: List[str]):
    sentimentScores = []
    for tweet in allTweets:
        blob = TextBlob(tweet)
        sentimentScores.append(blob.sentiment.polarity)

    return sentimentScores

def generate_average_sentiment_score(keyword: str) -> int:
    tweets = getTweets(keyword)
    tweetsClean = cleanTweets(tweets)
    sentimentScores = getSentiment(tweetsClean)

    average_score = statistics.mean(sentimentScores)

    return average_score

if __name__ == "__main__":

    print("What does the twitter prefer?")
    first = input()
    print("or")
    second = input()


    fist_score = generate_average_sentiment_score(first)
    second_score = generate_average_sentiment_score(second)

    if(first > second):
        print(f"The randomly selected 30 twitters would prefer {first} over {second}.")
    else:
        print(f"The randomly selected 30 twitters would prefer {second} over {first}.")


