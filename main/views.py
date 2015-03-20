from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main.forms import UserProfileForm
from main.models import *

def splash(request):
    return render(request, 'splash.html')

def how_it_works(request):
    return render(request, 'main/how_it_works.html')

def notifications(request):
    context_dict = {}
    return render(request, 'main/notifications.html', context_dict)

def about(request):
    return render(request, 'main/about.html')


def profile(request, user_id = None):
    if user_id is not None:
        context_dict = {'user': User.objects.get(id=user_id)}
    else:
        context_dict = {'user': User.objects.get(id=request.user.id)}
    try:
        context_dict['profile'] = UserProfile.objects.get(user=context_dict['user'])
    except:
        context_dict['profile'] = None

    return render(request, 'registration/profile.html', context_dict)

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

@login_required
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = None
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_updated = profile_form.save(commit=False)
            if user_profile is None:
                profile_updated.user = User.objects.get(id=request.user.id)
            if 'picture' in request.FILES:
                try:
                    profile_updated.picture = request.FILES['picture']
                except:
                    pass
            profile_updated.save()
            return redirect('myprofile')
    form = UserProfileForm(instance=user_profile)
    return render(request, 'registration/profile_edit.html', {'profile_form': form})

# Timetabling
def avail(request):
    context_dict = {}
    return render(request, 'main/avail.html', context_dict)