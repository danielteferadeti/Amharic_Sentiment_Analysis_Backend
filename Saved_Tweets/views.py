import imp
from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
# This is a request handler Class

def say_hello(request):
    return render(request, 'hello.html')