import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Consumer_API_key_REDACTED", "Consumer_API_secret_REDACTED")
auth.set_access_token("Access_token_REDACTED", "Access_secret_REDACTED")

# Create API object
api = tweepy.API(auth)
# bot_tweet could be any variable, but it represents tweets from @BI_lyricsbot
for bot_tweet in tweepy.Cursor(api.search, q='from:BI_lyricsbot').items(1):
	try:
		print('Attempting to retweet.')
		bot_tweet.retweet()
		print('Successfully retweeted.')

	except tweepy.TweepError as error:
		print('Error. Retweet not successful. Reason: ')
		print(error.reason)

	except StopIteration:
		break
'''
code taken from https://github.com/0xGrimnir/Simple-Retweet-Bot/blob/master/retweet.py
'''
'''
# To test access to Twitter
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
'''

'''
api.update_status("This is test tweet number 3. I'm making another boniverbot1.5. I will delete this tweet if it works.")
'''
