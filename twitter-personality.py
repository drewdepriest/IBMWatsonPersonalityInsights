import tweepy
import csv
import requests
import json
import sys

# twitter credentials
consumer_key = "b9i9pr9z52oc5qR7lMjbF0KBZ"
consumer_secret = "sFZv8MmchhjqgLUGKfigsVd88hTruPirOr3P4ujojcDump4HoH"
access_token = "47670288-rgWq0PJlBrvAnRrJCXOjbIpupLPLu6xySVqgB7L35"
access_token_secret = "SQ8tYy3FxlT8hIFQVH1UpDdujVZedGbuXKy31o5inFLN6"

# watson credentials
username = "8c17a986-a308-4959-8d1f-33bd23f6efc5"
password = "wEtRWJMlkcoV"

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))

	# just grab the context of each tweet, not the ID or the timestamp
	outtweets = ''.join(str(tweet.text.encode("utf-8")) for tweet in alltweets)

	# make the call to IBM Watson	
	response = requests.post("https://gateway.watsonplatform.net/personality-insights/api/v2/profile",
         auth=(username, password),
         headers = {"content-type": "text/plain"},
         data = outtweets
         )

	jsonProfile = json.loads(response.text)

	print "\n Analyzing Twitter user @" + str(sys.argv[1])

	# gets the array of personality traits
	traits = jsonProfile['tree']['children'][0]['children'][0]['children']

	print "\n *** Personality Traits *** "
	for trait in traits:
		print '{0:.2f}'.format(trait['percentage']*100) + '% - ' + trait['name']

		for subtrait in trait['children']:
				print '-- ' + '{0:.2f}'.format(subtrait['percentage']*100) + '% - ' + subtrait['name'] 

	# gets the array of needs
	needs = jsonProfile['tree']['children'][1]['children'][0]['children']
	print "\n *** Needs *** "
	for need in needs:
		print '{0:.2f}'.format(need['percentage']*100) + '% - ' + need['id']	

	# gets the array of values
	values = jsonProfile['tree']['children'][2]['children'][0]['children']
	print "\n *** Values *** "
	for value in values:
		print '{0:.2f}'.format(value['percentage']*100) + '% - ' + value['id']	

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets(str(sys.argv[1]))


