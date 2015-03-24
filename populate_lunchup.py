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

def add_user_profile(user, fullName, email, about, picture):
    p = UserProfile.objects.get_or_create(user=user, fullName=fullName,
                                          publicEmail=email, about=about, picture=picture)[0]
    return p


def add_feedback(content, rating, recipient, author, time, lunch):
    f = Feedback.objects.get_or_create(content=content, rating=rating,
                                       recipient=recipient, author=author,
                                       time=time, lunch=lunch)[0]
    return f


def add_university(university):
    u = University.objects.get_or_create(domain=university)
    return u


def add_time(time, day):
    t = TimeInterval.objects.get_or_create(time=time,
                                           day=day)
    return t


def add_notification(user1, user2, accepted1, accepted2, available):
    n = Notification.objects.get_or_create(userOne=user1, userTwo=user2,
                                           acceptedOne=accepted1, acceptedTwo=accepted2, available=available)
    return n


def add_interest(name):
    i = Interest.objects.get_or_create(name=name)
    return i


def add_lunch(user1, user2, date):
    l = Lunch.objects.get_or_create(userOne=user1, userTwo=user2, date=date)
    return l


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
    # Add interests
    football = add_interest(name='football')
    swimming = add_interest(name='swimming')
    going_out = add_interest(name='going out')
    reading = add_interest(name='reading')

    # Add unis
    glasgow = add_university(university='Glasgow University')

    # Users
    om = add_user('omar', '2098877q@student.gla.ac.uk', 'notgonnaguess')
    om.save()
    ju = add_user('eust', '2095666e@student.gla.ac.uk', 'notgonnaguessrly')
    ju.save()
    am = add_user('amyx', '2195152a@student.gla.ac.uk', 'ahaha')
    am.save()
    # User profiles
    Omar = add_user_profile(om, 'Omar Tufail', 'Blah@blah.co.uk',
                            'about me', 'profile_images/omar.jpg')
    Omar.interests.add(going_out, reading, football)
    Omar.university.add(glasgow)
    Omar.availability.add(sat13, fri14)
    Omar.save()

    Justas = add_user_profile(ju, 'Justas Bikulcius', 'Blah2@blah.co.uk'
                                                           'about me', 'profile_images/justas.jpg')
    Justas.interests.add(going_out)
    Justas.interests.add(swimming)
    Justas.university.add(glasgow)
    Justas.availability.add(sat13)
    Justas.availability.add(wed15)
    Justas.save()

    Amy = add_user_profile(am, 'Amy Rose', 'Blah3@blah.co.uk', 'about me',
                           'profile_images/amy.jpg')
    Amy.interests.add(going_out)
    Amy.interests.add(swimming)
    Amy.availability.add(wed15)
    Amy.availability.add(thu16)
    Amy.university.add(glasgow)
    Amy.save()


    # Feedback
    #forOmar = add_feedback('it was good', '4', Omar, Amy, time, lunch)
# Start execution here!
if __name__ == '__main__':
    print "Starting LunchUp population script..."
    populate()