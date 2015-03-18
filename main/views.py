from django.http import HttpResponse
from django.shortcuts import render
from main.models import *

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


'''def register_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = User.objects.get(id=request.user.id)
            if 'picture' in request.FILES:
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
            profile.save()
            return redirect('index')
    else:
        profile_form = UserProfileForm()
    return render(request, 'registration/profile_registration.html', {'profile_form': profile_form})
'''
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