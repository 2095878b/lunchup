from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax
from main.models import *

@login_required
@ajax
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if request.POST['name'] == "about":
            user_profile.about = request.POST['value']
        if request.POST['name'] == "interests":
            user_profile.interests = request.POST['value']
        if request.POST['name'] == "fullName":
            user_profile.fullName = request.POST['value']
        if request.POST['name'] == "publicEmail":
            user_profile.publicEmail = request.POST['value']
        user_profile.save()
    except:
        return {'status': 'error', 'msg': 'Unable to save field.'}

@login_required
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

@login_required
@ajax
def get_avail(request):
    up = UserProfile.objects.get(user=request.user)
    return up.availability.all()

@login_required
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

@login_required
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

