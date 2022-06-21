from http import client
import imp
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from Crowdsource.models import Crowdsource_Sentence
import json

# class Testviews(TestCase):
    
#     def test_all_crowdsourse_GET(self):
#         url = "/api/crowdsource/all_crowdsource_sentences/"
#         client = Client()
#         response = client.get(url)
        
#         self.assertEquals(response.status_code, 200)




