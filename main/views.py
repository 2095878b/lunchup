from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def splash(request):
    return render(request, 'splash.html')

def index(request):
    context_dict = {}
    return render(request, 'main/index.html', context_dict)

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    context_dict = {}
    return render(request, 'main/profile.html', context_dict)
# Timetabling
def availability(request):
    context_dict = {}
    return render(request, 'main/availability.html', context_dict)

def messages(request):
    context_dict = {}
    return render(request, 'main/message.html', context_dict)
# Having the ability to browse lunch history could be useful
def history(request):
    context_dict = {}
    return render(request, 'main/history.html', context_dict)