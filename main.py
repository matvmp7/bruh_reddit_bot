import praw
import config
import time
import os

def bot_login():
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "Bruh Bot")
	return r

def run_bot(r, comments_replied_to):
	print "Searching for Bruh comments"

	for comment in r.subreddit('askreddit').comments(limit=1000):
		if "bruh" in comment.body and comment.id not in comments_replied_to:
			print "Found \"Bruh\" in comment " + comment.id
			comment.reply("[...athkayosaurus](https://en.wikipedia.org/wiki/Bruhathkayosaurus)")
			print "Replied to comment " + comment.id 

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print "Sleeping for 10 seconds..."
	time.sleep(10)


def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)
	
	return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
print comments_replied_to

while True:
	run_bot(r, comments_replied_to)

