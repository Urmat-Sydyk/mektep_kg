from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import models


# Create your views here.

def index(request):
    print(request)
    return HttpResponse("Main")
