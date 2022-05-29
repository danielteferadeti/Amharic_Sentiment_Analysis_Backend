"""Amharic_Sentiment_Analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Saved_Tweets/', include('Saved_Tweets.urls')),
    
    #REST API PATHS
    path('api/saved_tweets/', include('Saved_Tweets.api.urls', 'saved_tweet_api')),
    path('api/crowdsource/', include('Crowdsource.api.urls', 'crowdsource_api'))
]
