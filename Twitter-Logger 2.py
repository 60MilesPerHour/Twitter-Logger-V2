import tweepy
import sys
import randfacts
import tweeterid
from API_Keys import consumer_key, consumer_secret, access_token, access_token_secret

search_hashtag = '#Enter_Hashtag_Here'
search_user = '@Enter_Twitter_Handle'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def Logger(message, user_of_tweet):
    appendFile = open('Twitter-Logger.txt','a')
    appendFile.write('### Logged Tweet ###' + '\n')
    appendFile.write('Message: ' + message + '\n' + '\n')
    appendFile.write('User: ' + user_of_tweet + '\n' + '\n')
    appendFile.close()

def retweet(target):
    for tweet in tweepy.Cursor(api.search_tweets, target).items(25):
        try:
            tweet.retweet()
            message = tweet.text
            user_of_tweet = tweeterid.id_to_handle(tweet.user.id)
            Logger(message, user_of_tweet)
            api.update_status(randfacts.get_fact() + '\n \n' + 'Random Fact Generator')
        except tweepy.TweepyException:
            break
        except StopIteration:
            break
    else:
        sys.exit()

retweet(target=search_hashtag)
retweet(target=search_user)