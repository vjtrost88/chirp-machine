
import sys
import pandas as pd
import numpy as np
from datetime import datetime

def add_tweet(tweets):
	'''
		run this so i can append tweets to my file
	'''
	print("Enter your tweet: \n")
	tweet = sys.stdin.read()
	if not tweet:
		print("Empty tweet.")
		return(tweets)

	time_entered = datetime.now()
	status = "not-posted"
	time_posted = np.NaN

	row = [time_entered, tweet, status, time_posted]
	tweets.loc[len(tweets)] = row

	print("Tweet has been appended.")

	return(tweets)


def main():

	tweets = pd.read_csv("tweets.csv")
	keep_going = True
	while(keep_going):
		tweets = add_tweet(tweets)
		val = input("Keep going? Enter y/n: ")
		if val == 'y':
			keep_going = True
		elif val == 'n':
			keep_going = False
		else:
			print("Please enter a valid value.")
	
	tweets.to_csv("tweets.csv", index=False)

if __name__ == '__main__':
	main()	
