# use Reddit public APIs to extract data. I will be using the PRAW library to interact with the Reddit API. I will be extracting data from the subreddit r/dataengineering.
# The data will be extracted in JSON format and saved to a file named data.json.
import praw
import json

# Create a Reddit instance
reddit = praw.Reddit(client_id='my_client_id',
                     client_secret='my_client_secret',
                     user_agent='my_user_agent')

# Extract data from the subreddit r/dataengineering
data = []
for submission in reddit.subreddit('dataengineering').hot(limit=10):
    data.append({
        'title': submission.title,
        'score': submission.score,
        'url': submission.url,
        'comments': submission.num_comments
    })
