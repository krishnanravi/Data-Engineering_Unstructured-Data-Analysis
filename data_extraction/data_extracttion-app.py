# use Reddit public APIs to extract data. I will be using the PRAW library to interact with the Reddit API. I will be extracting data from the subreddit r/dataengineering.
# The data will be extracted in JSON format and saved to a file named data.json.
import os

import praw
import pandas as pd

# Create a Reddit instance
reddit = praw.Reddit(client_id=os.environ['client_id'],
                     client_secret=os.environ['client_secret'],
                     user_agent='dev')

# how to generate

# Extract data from the subreddit r/dataengineering
data = []
for submission in reddit.subreddit('dataengineering').hot(limit=10):
    data.append({
        'title': submission.title,
        'author': submission.author.name,
        'date': submission.created_utc,
        'num_comments': submission.num_comments,
        'post': submission.selftext,
        'url': submission.url,
        'score': submission.score,
        'upvotes': submission.ups,
        'downvotes': submission.downs,
        'awards': submission.total_awards_received,
        'crossposts': submission.num_crossposts
    })

data_df = pd.DataFrame(data)
data_df.to_json('data.json')
print('Data extracted successfully and saved to data.json')