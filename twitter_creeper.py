import tweepy as tw
import json

with open("key.json", "r") as f:
    key = json.load(f)

auth = tw.OAuthHandler(key['API_KEY'], key['API_SECRET_KEY'])
auth.set_access_token(key['ACCESS_TOKEN'], key['ACCESS_TOKEN_SECRET'])
api = tw.API(auth, wait_on_rate_limit=True)

#api.update_status("Hello World!")

search_words = "Canada"
date_since = '2019-01-01'

tweets = tw.Cursor(api.search, q=search_words, lang='en', since=date_since).items(5)

for tweet in tweets:
    print(tweet.text)
