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
    u = User.objects.get(username=request.user.username)
    context_dict = {}
    try:
	up = UserProfile.objects.get(user=u)
    except:
	   up = None
	
    context_dict['user'] = u
    context_dict['userprofile'] = up
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