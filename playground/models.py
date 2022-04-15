from django.db import models

# Create your models here.
class Tweets_table(models.Model):
    tweet_id = models.CharField(max_length=200)
    tweet_content = models.CharField(max_length=500)
    tweet_location = models.CharField(max_length=500)
    tweet_classification = models.CharField(max_length=100)