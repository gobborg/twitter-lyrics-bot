import tweepy
import os
import random
from random import sample

print(os.getcwd())
os.chdir(os.path.dirname(__file__))

# To choose the line to tweet
def random_line(possible_output):
        lines = possible_output
        return random.sample(lines, 1)[0] # n= the number of items to print
#       print(random_line(possible_output))

def publictweet():
	#blah blah blah this is where the tweet code happens
	f = open("sorted-lyrics.txt","r")
	all_lines = f.read().splitlines()
	g = open("tweeted.txt","r") # a+ to read and append to the file
	output = g.read().splitlines()

	possible_output = [item for item in all_lines if item not in output]

	# range(n) where n= the number of times to be printed
	myline = random_line(possible_output)
	print(myline)

	# to append a new line to the output file
	file_object = open("tweeted.txt","a")
	file_object.write(myline+"\n")
	print(myline)

	# Create a tweet
	api.update_status(myline)

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Consumer_API_key_REDACTED", "Consumer_API_secret_REDACTED")
auth.set_access_token("Access_token_REDACTED", "Access_secret_REDACTED")

# Create API object
api = tweepy.API(auth)

'''
# To test access to Twitter
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Test tweet from Tweepy Python")
'''

publictweet()
