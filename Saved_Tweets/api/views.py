import imp
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Saved_Tweets.models import Analyzed_Tweets
from Saved_Tweets.api.serializers import Analyzed_Tweets_Serializer


@api_view(['GET', ])
def api_all_analyzed_tweets_view(request):
    try:
        all_analyzed_tweets = Analyzed_Tweets.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = Analyzed_Tweets_Serializer(all_analyzed_tweets, many=True)
        return Response(serializer.data)
    
@api_view(['GET', ])
def api_single_analyzed_tweet_view(request, tweetId):
    try:
        analyzed_tweet = Analyzed_Tweets.objects.get(tweetId = tweetId)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = Analyzed_Tweets_Serializer(analyzed_tweet)
        return Response(serializer.data)
    
@api_view(['PUT', ])
def api_update_analyzed_tweet_view(request, tweetId):
    try:
        analyzed_tweet = Analyzed_Tweets.objects.get(tweetId = tweetId)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = Analyzed_Tweets_Serializer(analyzed_tweet, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["Success"] = "Updated successfully!"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE', ])
def api_delete_analyzed_tweet_view(request, tweetId):
    try:
        analyzed_tweet = Analyzed_Tweets.objects.get(tweetId = tweetId)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        operation = analyzed_tweet.delete()
        data = {}
        if operation:
            data["Success"] = "delete Successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
    
@api_view(['POST', ])
def api_create_analyzed_tweet_view(request):
    analyzed_tweet = Analyzed_Tweets()
    if request.method == "POST":
        serializer = Analyzed_Tweets_Serializer(analyzed_tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
