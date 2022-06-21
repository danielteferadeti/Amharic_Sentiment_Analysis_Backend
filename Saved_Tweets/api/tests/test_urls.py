

import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from Saved_Tweets.api.views import api_all_analyzed_tweets_view
from Saved_Tweets.api.views import api_single_analyzed_tweet_view
from Saved_Tweets.api.views import api_update_analyzed_tweet_view
from Saved_Tweets.api.views import api_delete_analyzed_tweet_view
from Saved_Tweets.api.views import api_create_analyzed_tweet_view

class TestUrls(SimpleTestCase):
    
    def test_get_all_saved_tweets_url_is_resolved(self):
        url = "/api/saved_tweets/all_analyzed_tweets/"
        print(resolve(url))
        self.assertEquals(resolve(url).func, api_all_analyzed_tweets_view)
    
    def test_get_single_saved_tweets_url_is_resolved(self):
        url = "/api/saved_tweets/single_analyzed_tweet/123456789/"
        self.assertEquals(resolve(url).func, api_single_analyzed_tweet_view)
        
    def test_update_saved_tweets_url_is_resolved(self):
        url = "/api/saved_tweets/update_analyzed_tweet/12487462"
        self.assertEquals(resolve(url).func, api_update_analyzed_tweet_view)
        
    def test_delete_saved_tweets_url_is_resolved(self):
        url = "/api/saved_tweets/delete_analyzed_tweet/12345872"
        self.assertEquals(resolve(url).func, api_delete_analyzed_tweet_view)
        
    def test_create_saved_tweets_url_is_resolved(self):
        url = "/api/saved_tweets/create_analyzed_tweet"
        self.assertEquals(resolve(url).func, api_create_analyzed_tweet_view)