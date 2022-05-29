from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from Crowdsource.models import Crowdsource_Sentence

class Crowdsource_Sentence_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Crowdsource_Sentence
        fields = '__all__'