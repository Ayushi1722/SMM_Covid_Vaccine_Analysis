"""
Twitter data crawling and processing module.
"""

import tweepy
import pandas as pd
from ..config import (
    TWITTER_API_KEY,
    TWITTER_API_KEY_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)

def get_twitter_api():
    """
    Create and return an authenticated Twitter API object.
    """
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, 
        TWITTER_API_KEY_SECRET
    )
    auth.set_access_token(
        TWITTER_ACCESS_TOKEN, 
        TWITTER_ACCESS_TOKEN_SECRET
    )
    return tweepy.API(auth)

def get_mention_screen_names(array):
    """
    Extract screen names from user mention data.
    
    Args:
        array: List of user mention objects
        
    Returns:
        List of screen names
    """
    res = []
    if array:
        for x in array:
            res.append(x['screen_name'])
    return res

def form_query(tags):
    """
    Build a Twitter search query from hashtag list.
    
    Args:
        tags: List of hashtags
        
    Returns:
        String containing formatted query
    """
    res = ' OR '.join(tags)
    return res

def crawl_twitter(query, date_since, num_tweets, api):
    """
    Crawl Twitter for tweets matching the given query.
    
    Args:
        query: Search query string
        date_since: Date to start search from (YYYY-MM-DD)
        num_tweets: Number of tweets to retrieve
        api: Authenticated Twitter API object
        
    Returns:
        DataFrame containing tweet data
    """
    cols = [
        'username', 'created_at', 'truncated',
        'description', 'following', 'followers',
        'totaltweets', 'retweetcount', 'text',
        'hashtags', 'user_mention', 'retweetScreenNames'
    ]
    db = pd.DataFrame(columns=cols)
    tweets = tweepy.Cursor(
        api.search_tweets,
        q=query,
        lang="en",
        since_id=date_since,
        tweet_mode='extended'
    ).items(num_tweets)
    
    for x in tweets:
        screen_name = x.user.screen_name
        created_date = x.created_at
        truncated = x.truncated
        description = x.user.description
        following = x.user.friends_count
        followers = x.user.followers_count
        total_tweets = x.user.statuses_count
        retweet_count = x.retweet_count
        hash_tags = x.entities['hashtags']
        mention = x.entities['user_mentions']
        mention_screen_names = get_mention_screen_names(mention)
        retweet_screen_names = ''
        
        try:
            text = x.retweeted_status.full_text
            retweet_screen_names = x.retweeted_status.user.screen_name
        except AttributeError:
            text = x.full_text
            
        tweet_data = [
            screen_name, created_date, truncated,
            description, following, followers,
            total_tweets, retweet_count, text,
            hash_tags, mention_screen_names, retweet_screen_names
        ]
        
        db.loc[len(db)] = tweet_data
        
    return db 