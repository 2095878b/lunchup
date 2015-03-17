from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def splash(request):
    return HttpResponse('OK')

def index(request):
    return HttpResponse('OK')

def about(request):
    return HttpResponse('OK')

def profile(request):
    return HttpResponse('OK')

# Timetabling
def availability(request):
    return HttpResponse('OK')

def messages(request):
    return HttpResponse('OK')
# Having the ability to browse lunch history could be useful
def history(request):
    return HttpResponse('OK')