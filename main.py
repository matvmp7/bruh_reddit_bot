import praw
import config
import time
import os

def bot_login():
	reddit = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "Bruh Bot")
	return reddit

def run_bot(reddit, comments_replied_to):
	print "Searching for Bruh comments"

	for comment in reddit.subreddit('test').comments(limit=25):
		if "bruh" in comment.body and comment.id not in comments_replied_to and not comment.author != reddit.user.me():
			print "Found \"Bruh\" in comment " + comment.id
			comment.reply("[...athkayosaurus](https://en.wikipedia.org/wiki/Bruhathkayosaurus)")
			print "Replied to comment " + comment.id 

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	for comment in reddit.subreddit('askreddit').comments(limit=25):
			if "bruh" in comment.body and comment.id not in comments_replied_to and not comment.author != reddit.user.me():
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


reddit = bot_login()
comments_replied_to = get_saved_comments()


while True:
	run_bot(reddit, comments_replied_to)


