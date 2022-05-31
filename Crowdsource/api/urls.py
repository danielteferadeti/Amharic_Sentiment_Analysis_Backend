from django.urls import path
from Crowdsource.api.views import api_all_crowdsource_sentences_view
from Crowdsource.api.views import api_single_crowdsource_sentence_view
from Crowdsource.api.views import api_update_crowdsource_sentence_view
from Crowdsource.api.views import api_delete_crowdsource_sentence_view
from Crowdsource.api.views import api_create_crowdsource_sentence_view
# from Crowdsource.api.views import api_check_sentence_view

app_name = 'Saved_Tweets'

urlpatterns = [
    path('all_crowdsource_sentences/', api_all_crowdsource_sentences_view, name="detail"),
    path('single_crowdsource_sentence/', api_single_crowdsource_sentence_view, name="detail"),
    path('update_crowdsource_sentence/<Id>', api_update_crowdsource_sentence_view, name="update"),
    path('delete_crowdsource_sentence/<Id>', api_delete_crowdsource_sentence_view, name="delete"),
    path('create_crowdsource_sentence', api_create_crowdsource_sentence_view, name="create"),
]