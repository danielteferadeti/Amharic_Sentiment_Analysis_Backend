from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweets_table

# Create your views here.

def say_hello(request):
    
    all_tweets = Tweets_table.objects.values()
    
    # return render(request, 'hello.html', {'tweets': all_tweets})
    return HttpResponse(all_tweets)
    #36:36