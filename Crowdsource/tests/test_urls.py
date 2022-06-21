

import imp
from django.test import SimpleTestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from Crowdsource.api.views import api_all_crowdsource_sentences_view
from Crowdsource.api.views import api_single_crowdsource_sentence_view
from Crowdsource.api.views import api_update_crowdsource_sentence_view
from Crowdsource.api.views import api_delete_crowdsource_sentence_view
from Crowdsource.api.views import api_create_crowdsource_sentence_view
from Crowdsource.api import urls

class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resolved(self):
        url = reverse('list')
        print(resolve(url))
        