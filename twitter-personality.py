import tweepy
import requests
import json
import sys

# twitter credentials
consumer_key = "TWITTER_CONSUMER_KEY"
consumer_secret = "TWITTER_CONSUMER_SECRET"
access_token = "TWITTER_ACCESS_TOKEN"
access_token_secret = "TWITTER_ACCESS_TOKEN_SECRET"

# watson credentials
username = "WATSON_PI_USERNAME"
password = "WATSON_PI_PASSWORD"

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	try:
		api = tweepy.API(auth)

		#make initial request for most recent tweets (200 is the maximum allowed count)
		new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	except tweepy.TweepError as e:
		print e.message[0]['message']	# prints error message
		print "Error code: " + str(e.message[0]['code'])  # prints error code
		return	# stops the entire function from continuing

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


