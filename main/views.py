from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.forms import UserProfileForm
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


def add_details(request):
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

def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = None
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_updated = profile_form.save(commit=False)
            if users_profile is None:
                profile_updated.user = User.objects.get(id=request.user.id)
            if 'picture' in request.FILES:
                try:
                    profile_updated.picture = request.FILES['picture']
                except:
                    pass
            profile_updated.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
        return render(request, 'registration/profile_edit.html', {'profile_form': form})

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