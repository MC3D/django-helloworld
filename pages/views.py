# from django.shortcuts import render # muted
from django.http import HttpResponse # allows us to return a response object to the user

# Create your views here.

def homePageView(request):
    return HttpResponse('Hello, World!')
