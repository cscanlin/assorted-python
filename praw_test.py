import praw
r = praw.Reddit(user_agent='my_cool_application')
user = r.get_redditor('cscanlin')
comments = user.get_comments(limit=10)
print([str(comment) for comment in comments])
# submissions = r.get_subreddit('opensource').get_hot(limit=5)
# print([str(x) for x in submissions])
