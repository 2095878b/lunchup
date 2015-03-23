from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_ajax.decorators import ajax
from main.forms import UserProfileForm
from main.models import *


# TODO: Major bug here. edit_profile can only save one field
# the other fields get cleared for some reason
@ajax
@login_required
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        profile_form = UserProfileForm(data={request.POST['name']:request.POST['value']},instance=user_profile)
        if profile_form.is_valid():
            user_profile = profile_form.save(commit=False)
            user_profile.save()
    except:
        return {'status':'error', 'msg':'Unable to save field.'}

@ajax
def get_interests(request):
    return Interest.objects.all()

@login_required
def upload_picture(request):
    if request.method == 'POST':
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            if 'picture' in request.FILES:
                try:
                    user_profile.picture = request.FILES['picture']
                    user_profile.save()
                except:
                    pass
        except:
            pass
        return redirect('/')
    else:
        return render(request, 'registration/upload_picture.html')


def splash(request):
    return render(request, 'splash.html')

# For now this serves as our splash page
#@login_required
def how_it_works(request):
    return render(request, 'main/how_it_works.html')

@login_required
def notifications(request):
    context_dict = {}
    return render(request, 'main/notifications.html', context_dict)

def about(request):
    return render(request, 'main/about.html')

# TODO: If profile is empty - it does not participate in 'matchmaking'
def profile(request, user_id = None):
    if user_id is not None:
        context_dict = {'user': User.objects.get(id=user_id)}
    else:
        context_dict = {'user': User.objects.get(id=request.user.id)}
    try:
        context_dict['profile'] = UserProfile.objects.get(user=context_dict['user'])
    except:
        context_dict['profile'] = None

    # Booleans don't work in templates for some reason, using None to avoid that
    if user_id is None or user_id == request.user.id:
        context_dict['myprofile'] = True
    else:
        context_dict['myprofile'] = None
    return render(request, 'registration/profile.html', context_dict)

# Timetabling
def avail(request):
    context_dict = {}
    return render(request, 'main/avail.html', context_dict)