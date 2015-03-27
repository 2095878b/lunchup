from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from main.models import *

# Matchmaking algorithm
def magic(request):
    data = ""
    try:
        Notification.objects.all().delete()
        allprofiles = UserProfile.objects.all()
        apL = len(allprofiles)
        for user1 in range(0, apL):
            for user2 in range(user1 + 1, apL):
                data += 'CMP ID' + str(allprofiles[user1].id) + '(' + allprofiles[user1].user.email + ')' + \
                    ' ID'+str(allprofiles[user2].id)+'('+allprofiles[user2].user.email+')<br>'
                if user1 != user2:
                    if allprofiles[user1].university == allprofiles[user2].university:
                        for t in allprofiles[user1].availability.all():
                            data += str(t.day) + str(t.time) + ' && '
                        data += '<br>'
                        for t in allprofiles[user2].availability.all():
                            data += str(t.day) + ' at ' + str(t.time) + ' && '
                        data += '<br>'
                        for t in allprofiles[user1].availability.all():
                            if t in allprofiles[user2].availability.all():
                                data += 'MATCH! ' + str(t.day) + ' at ' + str(t.time) + '<br><br>'
                                n = Notification.objects.get_or_create(userOne=allprofiles[user1],
                                                                       userTwo=allprofiles[user2],
                                                                       acceptedOne=False,
                                                                       acceptedTwo=False)[0]
                                n.available.add(t)
                                n.save()
                    else:
                        data += ' SKIP<br>'
                else:
                    data += ' SKIP<br>'
    except Exception as inst:
        print inst
        return HttpResponse("You have to RUB IT three times." + data)
    return HttpResponse('The genie was let out of the lamp.<br>' + data)

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
        return redirect('/profile')
    else:
        return render(request, 'registration/upload_picture.html')


def splash(request):
    return render(request, 'main/intro.html')

@login_required
def how_it_works(request):
    return render(request, 'main/how_it_works.html')

@login_required
def notifications(request):
    context_dict = {}
    try:
        context_dict['userprofile'] = UserProfile.objects.get(user=request.user)
        context_dict['notifications'] = \
            Notification.objects.filter((Q(userOne=context_dict['userprofile']) & Q(acceptedOne=False)) | (Q(userTwo=context_dict['userprofile']) & Q(acceptedTwo=False)))
        context_dict['matches'] = \
            Notification.objects.filter((Q(acceptedOne=True) & Q(acceptedTwo=True)) & (Q(userOne=context_dict['userprofile']) | Q(userTwo=context_dict['userprofile'])))
    except:
        pass
    return render(request, 'main/notifications.html', context_dict)

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def profile(request, user_id=None):
    if request.method == "POST" and request.POST['recipient'] != request.user.id:
        try:
            feedback = Feedback(content=request.POST['content'],
                                recipient=UserProfile.objects.get(id=request.POST['recipient']),
                                author=UserProfile.objects.get(user=request.user))
            feedback.save()
        except:
            pass
    if user_id is not None:
        context_dict = {'user': User.objects.get(id=user_id)}
    else:
        context_dict = {'user': User.objects.get(id=request.user.id)}
    try:
        context_dict['profile'] = UserProfile.objects.get(user=context_dict['user'])
        context_dict['feedback'] = Feedback.objects.filter(recipient=context_dict['profile']).all()
    except:
        context_dict['profile'] = None

    # Booleans don't work in templates for some reason, using None to avoid that
    if user_id is None or user_id == request.user.id:
        context_dict['myprofile'] = True
    else:
        context_dict['myprofile'] = None
    return render(request, 'registration/profile.html', context_dict)

# Timetabling
@login_required
def avail(request):
    context_dict = {}
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        context_dict['availabilities'] = user_profile.availability.all()
    except:
        pass
    return render(request, 'main/avail.html', context_dict)
