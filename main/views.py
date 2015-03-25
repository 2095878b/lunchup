from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_ajax.decorators import ajax
from django.db.models import Q
from main.models import *

@ajax
@login_required
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if request.POST['name'] == "about":
            user_profile.about = request.POST['value']
        if request.POST['name'] == "fullName":
            user_profile.fullName = request.POST['value']
        if request.POST['name'] == "publicEmail":
            user_profile.publicEmail = request.POST['value']
        user_profile.save()
    except:
        return {'status': 'error', 'msg': 'Unable to save field.'}

@ajax
def accept_or_decline(request):
    try:
        notif = Notification.objects.get(id=request.POST['notifid'])
        if request.POST['accept'] == 'y':
            if notif.userOne.user == request.user:
                notif.acceptedOne = True
            if notif.userTwo.user == request.user:
                notif.acceptedTwo = True
            notif.save()
        else:
            # Security measure
            if notif.userOne.user == request.user or notif.userTwo.user == request.user:
                notif.delete()
    except:
        return {'status': 'error', 'msg': 'Could not accept/decline.'}

@ajax
def get_avail(request):
    up = UserProfile.objects.get(user=request.user)
    return up.availability.all()

@ajax
def add_avail(request):
    time = int(request.POST['time'])
    day = str(request.POST['day'])
    if (time not in [12, 13, 14, 15] or day not in \
            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
        return {'status':'error', 'msg':'Invalid data'}
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        availab = TimeInterval.objects.get(time=time, day=day)
        user_profile.availability.add(availab)
        user_profile.save()
    except:
        return {'status':'error', 'msg':'Something went wrong. Please relog.'}

@ajax
def rm_avail(request):
    time = int(request.POST['time'])
    day = str(request.POST['day'])
    if (time not in [12, 13, 14, 15] or day not in \
            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
        return {'status':'error', 'msg':'Invalid data'}
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        availab = TimeInterval.objects.get(time=time, day=day)
        user_profile.availability.remove(availab)
        user_profile.save()
    except:
        return {'status':'error', 'msg':'Something went wrong. Please relog.'}


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
    try:
        context_dict['userprofile'] = UserProfile.objects.get(user=request.user)
        context_dict['notifications'] = \
            Notification.objects.filter((Q(userOne=context_dict['userprofile']) & Q(acceptedOne=False)) | (Q(userTwo=context_dict['userprofile']) & Q(acceptedTwo=False)))
    except:
        pass
    return render(request, 'main/notifications.html', context_dict)

def about(request):
    return render(request, 'main/about.html')

# TODO: If profile is empty - it does not participate in 'matchmaking'
def profile(request, user_id=None):
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
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        context_dict['availabilities'] = user_profile.availability.all()
    except:
        pass
    return render(request, 'main/avail.html', context_dict)