import praw
import config
import time
import os

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id= config.client_id,
            client_secret = config.client_secret,
            user_agent = "Tester")
    print "Logged in!"
    return r

def run_bot(r, comments_replied_to):
    print "Searching for comments..."
 
    for comment  in r.subreddit('wholesomememes').comments(limit=1000):
        if " hate " in comment.body and comment.id not in comments_replied_to and not comment.author == r.user.me():
            print "String found"
            comment.reply("Hate is a strong word, I prefer 'Strong dislike'. I am a bot created by a undergrad student on a rasberry pi, and will be running over night for testing purposes, and to remind people hate is a very strong word.Hate is a strong word. ")
            print "replied to comment " + comment.id
            comments_replied_to.append(comment.id)
            
            with open("comments.txt","a") as f:
                f.write(comment.id + "\n")
    #Sleep for 10 seconds
    print "Sleeping for 2 seconds"
    time.sleep(2)
def get_saved_comments():
    if not os.path.isfile("comments.txt"):
        comments_replied_to=[]
    else:
        with open ("comments.txt", "r") as f:
                comments_replied_to= f.read()
                comments_replied_to= comments_replied_to.split("\n")
                comments_replied_to = filter(None, comments_replied_to)
                
    return comments_replied_to


r = bot_login()
comments_replied_to=get_saved_comments()
while True:
    
    run_bot(r, comments_replied_to)