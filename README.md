I wrote this for the Twitter v1 API.
The new version, in PHP, runs on [archox.net](archox.net).

# Twitter lyrics bot

Twitter lyrics bot is a Python code to create a Twitter bot that tweets song lyrics.

*configbot.py* is Python code to create a bot that will automatically tweet one random line from a corpus without replacement.  
*retweetbot.py* is the Python code to create a bot that will automatically retweet tweets from an account.

*configbot.py* works by comparing two files: a list of all possible lyrics, and a list of all tweeted lyrics. It then chooses a random line from the difference, and tweets it. It then appends the newly tweeted lyric to the list of tweeted lyrics.  
In my files, the list of all possible lyrics is sorted alphabetically.  
To keep the bot running, I have it in a virtual machine, and it is scheduled with a cronjob to run every 24 hours.

*retweetbot.py* searches the twitter api for tweets by my bot, and then automatically retweets them to my main account. It is also hosted in virtual machine, and it is schedule with a cronjob to run every 24 hours + 1 minute after the *configbot.py* program.  

## If you want to create your own bot...  
you will need to create a new twitter account for the bot.  
- For the email address associated with the account, if you use gmail, you can use *gmailhandle+twittername(at)gmail(.)com.* Twitter will think that it is a unique email address, but all emails will go to your main account. Verify your account email.  
- Go to developer.twitter.com to apply for developer keys.  
- Once you have developer keys, go to apps.twitter.com to create a new app.  
- In apps.twitter.com, click the gear icon for Settings, and make sure that App Permissions are set to "read and write."  
- Scroll up to "Keys and tokens", and get your Consumer Keys and Authentification Tokens. I saved mine in a .txt file.  
---
- Make sure that you have [tweepy python](https://docs.tweepy.org/en/latest/install.html) installed before you start coding.  
