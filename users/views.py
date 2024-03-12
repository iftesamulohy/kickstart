from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def members(request):
    return HttpResponse("Hello world!")

def viewfuntion(request):
    return HttpResponse("Another Response")