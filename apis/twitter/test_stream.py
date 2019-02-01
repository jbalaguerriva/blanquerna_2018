# https://tweepy.readthedocs.io/en/v3.5.0/streaming_how_to.html
# https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter.html
# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pprint
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print("=======================================================================================================")
        pprint.pprint(json.loads(data))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, StdOutListener())
    stream.filter(track=['vox'])