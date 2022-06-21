

import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from Crowdsource.api.views import api_all_crowdsource_sentences_view
from Crowdsource.api.views import api_single_crowdsource_sentence_view
from Crowdsource.api.views import api_update_crowdsource_sentence_view
from Crowdsource.api.views import api_delete_crowdsource_sentence_view
from Crowdsource.api.views import api_create_crowdsource_sentence_view

class TestUrls(SimpleTestCase):
    
    def test_get_all_crowdsource_url_is_resolved(self):
        url = "/api/crowdsource/all_crowdsource_sentences/"
        print(resolve(url))
        self.assertEquals(resolve(url).func, api_all_crowdsource_sentences_view)
    
    def test_get_single_crowdsource_url_is_resolved(self):
        url = "/api/crowdsource/single_crowdsource_sentence/"
        self.assertEquals(resolve(url).func, api_single_crowdsource_sentence_view)
        
    def test_update_crowdsource_url_is_resolved(self):
        url = "/api/crowdsource/update_crowdsource_sentence/2"
        self.assertEquals(resolve(url).func, api_update_crowdsource_sentence_view)
        
    def test_delete_crowdsource_url_is_resolved(self):
        url = "/api/crowdsource/delete_crowdsource_sentence/2"
        self.assertEquals(resolve(url).func, api_delete_crowdsource_sentence_view)
        
    def test_create_crowdsource_url_is_resolved(self):
        url = "/api/crowdsource/create_crowdsource_sentence"
        self.assertEquals(resolve(url).func, api_create_crowdsource_sentence_view)