from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from Saved_Tweets.models import Analyzed_Tweets

class Analyzed_Tweets_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Analyzed_Tweets
        fields = '__all__'