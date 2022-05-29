from django.db import models

# Create your models here.

class Analyzed_Tweets(models.Model):
    tweetId = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    hateValue = models.FloatField()
    loc_lat = models.FloatField()
    loc_lng = models.FloatField()
    dateOfTweet = models.CharField(max_length=200)
    dateOfPrediction = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tweetId