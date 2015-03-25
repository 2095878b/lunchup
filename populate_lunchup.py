import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lunchup.settings')

import django

django.setup()

from main.models import *


def add_user(username, email, password):
    try:
        u = User.objects.get(username=username)
    except:
        u = User.objects.create_user(username, email, password)
    return u

def add_user_profile(user, fullname, email, about, interests):
    p = UserProfile.objects.get_or_create(user=user, fullName=fullname,
                                          publicEmail=email, about=about, interests=interests)[0]
    return p


def add_feedback(content, recipient, author):
    f = Feedback.objects.get_or_create(content=content,
                                       recipient=recipient, author=author)[0]
    return f


def add_university(university):
    u = University.objects.get_or_create(domain=university)[0]
    return u


def add_time(time, day):
    t = TimeInterval.objects.get_or_create(time=time,
                                           day=day)[0]
    return t


def add_notification(user1, user2, accepted1, accepted2):
    n = Notification.objects.get_or_create(userOne=user1, userTwo=user2,
                                           acceptedOne=accepted1, acceptedTwo=accepted2, picture=None)[0]
    return n


#def add_interest(name):
#    i = Interest.objects.get_or_create(name=name)[0]
#    return i


# O(n^2), there's room for improvement
def make_matches():
    allprofiles = UserProfile.objects.all()
    apL = len(allprofiles)
    for user1 in range(0, apL/2 + 1):
        for user2 in range(apL - 1, apL/2 - 1, -1):
            if user1 != user2:
                if allprofiles[user1].university == allprofiles[user2].university:
                    for t in allprofiles[user1].availability.all():
                        if t in allprofiles[user2].availability.all():
                            n = add_notification(allprofiles[user1], allprofiles[user2], False, False)
                            n.available.add(t)
                            n.save()
def populate():
    # Populate time intervals
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = [str(i) for i in range(12, 16)]
    for day in days:
        for time in times:
            add_time(time=time, day=day)
    # Get some times
    sat13 = add_time(time=13, day='Saturday')
    wed15 = add_time(time=13, day='Wednesday')
    thu16 = add_time(time=13, day='Thursday')
    fri14 = add_time(time=13, day='Friday')

    # Add unis
    glasgow = add_university(university='Glasgow University')

    # Users
    om = add_user('omar', '2098877q@student.gla.ac.uk', 'root')
    om.save()
    ju = add_user('eust', '2095666e@student.gla.ac.uk', 'root')
    ju.save()
    am = add_user('amy', '2195152a@student.gla.ac.uk', 'root')
    am.save()
    # User profiles
    Omar = add_user_profile(om, 'Omar Tufail', 'Blah@blah.co.uk',
                            'about me', 'Going out, playing foodball, reading.')

    Omar.university = glasgow
    Omar.availability.add(sat13, fri14)
    Omar.save()

    Justas = add_user_profile(ju, 'Justas Bikulcius', 'Blah2@blah.co.uk',
                                                           'about me', 'Attending lectures, not doing drugs.')
    Justas.university = glasgow
    Justas.availability.add(sat13)
    Justas.availability.add(wed15)
    Justas.save()

    Amy = add_user_profile(am, 'Amy Rose', 'Blah3@blah.co.uk', 'about me', 'Listening to music and dancing.')

    Amy.availability.add(wed15)
    Amy.availability.add(thu16)
    Amy.university = glasgow
    Amy.save()

    #make_matches()
    # Feedback
    add_feedback('What a charmer!', Omar, Amy)
    add_feedback('I think I still owe you 40p...', Omar, Justas)
    add_feedback('Could have been better. Asshole was late.', Justas, Omar)
    add_feedback('We both like the same band, untitled artist.', Amy, Justas)
    add_feedback('We both like the same song, unknown track.', Justas, Amy)
# Start execution here!
if __name__ == '__main__':
    print "Starting LunchUp population script..."
    populate()