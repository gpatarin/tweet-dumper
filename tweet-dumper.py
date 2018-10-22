# Simple tweet-dumper from twitter
# Refer to https://github.com/sixohsix/twitter documentation for other API request.
# @author gpatarin

from twitter import *
import re

consumer_key = "consumerKEY"
consumer_secret = "consumerSECRET"

# You can leave these lines empty if you are only retrieving tweets from twitter.
token = ""
secret_token = ""


t = Twitter(
    auth=OAuth(token, secret_token, consumer_key, consumer_secret)
)

# Tab can be with only one username or more
twitter_accounts = ["username without @", "username without @"]


for i in twitter_accounts:

    # GET 200 tweets from the user account.
    jsonresult = t.statuses.user_timeline(screen_name=i, count=200, tweet_mode="extended")

    #Open an username.txt
    file = open(i + ".txt", 'w')
    output = ""

    for j in jsonresult:
        output += j['full_text']
        output += "\n\n"
        replacedoutput = re.sub('(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?\S', '', output)

    file.write(replacedoutput)
    file.close()
