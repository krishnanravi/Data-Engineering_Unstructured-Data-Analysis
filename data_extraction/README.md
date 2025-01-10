Alright. We are onto data extraction as a first step in our data pipeline. Lets crush it!

For this project I have decided to use Reddit public APIs to extract data. I will be using the PRAW library to interact with the Reddit API. I will be extracting data from the subreddit r/dataengineering. 
I will be extracting the following data:
1. Title of the post
2. Author of the post
3. Date of the post
4. Number of comments on the post
5. The post itself
6. The URL of the post
7. The score of the post
8. The number of upvotes and downvotes on the post
9. The number of awards on the post
10. The number of crossposts of the post
11. The number of awards on the post
12. The number of crossposts of the post

I will be extracting the data in the form of a pandas dataframe and then save it as a csv file. 

We have to decide on the data model for the data extraction. I am thinking of the following data model:
<br/>
<h3>Post</h3>
<ul>
    <li>title</li>
    <li>author</li>
    <li>date</li>
    <li>num_comments</li>
    <li>post</li>
    <li>url</li>
    <li>score</li>
    <li>upvotes</li>
    <li>downvotes</li>
    <li>awards</li>
    <li>crossposts</li>
</ul>

Generally it is best practice to keep the ingestion layer schema as close as possible to the source data. This will help us in tracing back data quality issues back to the exact step in the pipeline where the issue was introduced including the source.


