from django.urls import path
from Saved_Tweets.api.views import api_all_analyzed_tweets_view
from Saved_Tweets.api.views import api_single_analyzed_tweet_view
from Saved_Tweets.api.views import api_update_analyzed_tweet_view
from Saved_Tweets.api.views import api_delete_analyzed_tweet_view
from Saved_Tweets.api.views import api_create_analyzed_tweet_view

app_name = 'Saved_Tweets'

urlpatterns = [
    path('all_analyzed_tweets/', api_all_analyzed_tweets_view, name="detail"),
    path('single_analyzed_tweet/<tweetId>/', api_single_analyzed_tweet_view, name="detail"),
    path('update_analyzed_tweet/<tweetId>', api_update_analyzed_tweet_view, name="update"),
    path('delete_analyzed_tweet/<tweetId>', api_delete_analyzed_tweet_view, name="delete"),
    path('create_analyzed_tweet', api_create_analyzed_tweet_view, name="create")
]
