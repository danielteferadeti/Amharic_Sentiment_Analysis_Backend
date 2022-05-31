from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

# from django.conf import settings

from Crowdsource.models import Crowdsource_Sentence
from Crowdsource.api.serializers import Crowdsource_Sentence_Serializer


@api_view(['GET', ])
def api_all_crowdsource_sentences_view(request):
    try:
        all_crowdsource_sentence = Crowdsource_Sentence.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = Crowdsource_Sentence_Serializer(all_crowdsource_sentence, many=True)
        return Response(serializer.data)
    
@api_view(['GET', ])
def api_single_crowdsource_sentence_view(request):
    try:
        all_crowdsource_sentence = Crowdsource_Sentence.objects.filter(classification = "-1")
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = Crowdsource_Sentence_Serializer(all_crowdsource_sentence, many=True)
        return Response(serializer.data[0])
    
@api_view(['PUT', ])
def api_update_crowdsource_sentence_view(request, Id):
    try:
        crowdsource_sentence = Crowdsource_Sentence.objects.get(id = Id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = Crowdsource_Sentence_Serializer(crowdsource_sentence, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["Success"] = "Updated successfully!"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE', ])
def api_delete_crowdsource_sentence_view(request, Id):
    try:
        crowdsource_sentence = Crowdsource_Sentence.objects.get(id = Id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        operation = crowdsource_sentence.delete()
        data = {}
        if operation:
            data["Success"] = "delete Successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
    
@api_view(['POST', ])
def api_create_crowdsource_sentence_view(request):
    crowdsource_sentence = Crowdsource_Sentence()
    if request.method == "POST":
        serializer = Crowdsource_Sentence_Serializer(crowdsource_sentence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# tokenizer = Tokenizer(num_words=5000)

# joblib.dump(Pipeline,'model2.sav')

# def open_model():
#     models_folder = settings.BASE_DIR / 'Crowdsource' / 'api'
#     file_path = os.path.join(models_folder, os.path.basename("model2.sav"))
#     with open(file_path, 'rb') as f:
#         return pickle.load(f)
#     # return file_path

# model2 = joblib.load('model2.sav')

# def checker(test_word):
#     tw = tokenizer.texts_to_sequences([test_word])
#     tw = pad_sequences(tw,maxlen=200)
#     return tw

# @api_view(['POST', ])
# def api_check_sentence_view(request):
#     if request.method == "POST":
#         data=request.data
#         k = data["A"]
#         k = checker(k)
#         to_return = model2.predict(k).item()
#         return Response(data=to_return)