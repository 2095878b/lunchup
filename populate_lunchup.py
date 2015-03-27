import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lunchup.settings')

import django
import json

django.setup()

from main.models import *
from main.views import magic


def add_user(username, email, password):
    try:
        u = User.objects.get(username=username)
    except:
        u = User.objects.create_user(username, email, password)
    return u


def add_user_profile(user, fullname, email, about, interests, picture):
    p = UserProfile.objects.get_or_create(user=user, fullName=fullname,
                                          publicEmail=email, about=about, interests=interests, picture=picture)[0]
    return p


def add_feedback(content, recipient, author):
    f = Feedback.objects.get_or_create(content=content,
                                       recipient=recipient, author=author)[0]
    return f


def add_university(name, domain):
    u = University.objects.get_or_create(name=name, domain=domain)[0]
    return u


def add_time(time, day):
    t = TimeInterval.objects.get_or_create(time=time,
                                           day=day)[0]
    return t


def add_notification(user1, user2, accepted1, accepted2):
    n = Notification.objects.get_or_create(userOne=user1, userTwo=user2,
                                           acceptedOne=accepted1, acceptedTwo=accepted2)[0]
    return n


def populate():
    # Populate universities
    f = open("world_universities_and_domains.json")
    f = f.read()
    data = json.loads(f)
    for uni in data:
        if uni['country'] == 'United Kingdom':
            add_university(name=uni['name'], domain=uni['domain'])

    # Populate time intervals
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = [str(i) for i in range(12, 16)]
    for day in days:
        for time in times:
            add_time(time=time, day=day)

    # Get some times
    sat13 = add_time(time=13, day='Saturday')
    wed15 = add_time(time=15, day='Wednesday')
    thu16 = add_time(time=16, day='Thursday')
    fri14 = add_time(time=14, day='Friday')
    tue13 = add_time(time=13, day='Tuesday')
    thu15 = add_time(time=15, day='Thursday')

    # Add unis
    glasgow = University.objects.get(domain='gla.ac.uk')

    # Users
    te = add_user('test', '2096757p@student.gla.ac.uk', 'test')
    te.save()
    om = add_user('omar', '2098877q@student.gla.ac.uk', 'root')
    om.save()
    ju = add_user('eust', '2095666e@student.gla.ac.uk', 'root')
    ju.save()
    am = add_user('amyx', '2195152a@student.gla.ac.uk', 'root')
    am.save()
    ra = add_user('vj', '2080123v@student.gla.ac.uk', 'root')
    ra.save()
    bl = add_user('bliatch', '2078910A@student.gla.ac.uk', 'root')
    bl.save()
    zo = add_user('zoes', '2065610s@student.gla.ac.uk', 'root')
    zo.save()
    # User profiles

    test = add_user_profile(te, 'Test User', 'test@gmail.co.uk',
                            'I like being used to log on and play about with the app.',
                            'testing app and trying to break it', 'profile_images/test.jpg')

    test.university = glasgow
    test.availability.add(thu16)
    test.availability.add(fri14)
    test.availability.add(tue13)
    test.save()

    Omar = add_user_profile(om, 'Omar Tufail', 'omar@gmail.com',
                            'I love programming but I think its about time I move away from the screen.',
                            'Going out, playing foodball, reading.', 'profile_images/omar.jpg')

    Omar.university = glasgow
    Omar.availability.add(sat13)
    Omar.availability.add(fri14)
    Omar.availability.add(wed15)
    Omar.save()

    Justas = add_user_profile(ju, 'Justas Bikulcius', 'eustace@yahoo.com',
                              'I totally love studying but I think I would rather meet new people',
                              'Attending lectures, not doing drugs.', 'profile_images/justas.jpg')

    Justas.university = glasgow
    Justas.availability.add(sat13)
    Justas.availability.add(wed15)
    Justas.availability.add(tue13)
    Justas.save()

    Amy = add_user_profile(am, 'Amy Rose', 'xamyrosexx@aol.co.uk',
                           'Im tired of eating alone so would love to meet someone new over lunch ',
                           'Listening to music and dancing.',
                           'profile_images/amy.jpg')

    Amy.availability.add(wed15)
    Amy.availability.add(fri14)
    Amy.availability.add(thu16)
    Amy.university = glasgow
    Amy.save()

    Raj = add_user_profile(ra, 'Rajeevan Vijayakumar', 'vj96@live.co.uk',
                           'I think its time to take a break from the virtual space and meet someone in real life',
                           'Playing games and reking noobs.',
                           'profile_images/raj.jpg')

    Raj.university = glasgow
    Raj.availability.add(sat13)
    Raj.availability.add(thu16)
    Raj.availability.add(tue13)
    Raj.save()

    Blair = add_user_profile(bl, 'Blair Aitcheson', 'baitch96@hotmail.co.uk',
                             'Love surfing the net and love get mad with it', 'Listening to music and chilling',
                             'profile_images/blair.jpg')

    Blair.university = glasgow
    Blair.availability.add(fri14)
    Blair.availability.add(wed15)
    Blair.availability.add(thu15)
    Blair.save()

    Zoe = add_user_profile(zo, 'Zoe Thorn', 'zzthorn@live.co.uk', 'Love going to town and going on shopping sprees',
                           'Watching Movies and going out',
                           'profile_images/zoe.jpg')

    Zoe.university = glasgow
    Zoe.availability.add(fri14)
    Zoe.availability.add(wed15)
    Zoe.availability.add(tue13)
    Zoe.save()


    # Feedback
    add_feedback('What a charmer!', Omar, Amy)
    add_feedback('I think I still owe you 40p...', Omar, Justas)
    add_feedback('Could have been better. Asshole was late.', Justas, Omar)
    add_feedback('We both like the same band, untitled artist.', Amy, Justas)
    add_feedback('We both like the same song, unknown track.', Justas, Amy)
    add_feedback('Had a great lunch, thanks. Hope we can grab luch again.', Zoe, Raj)
    add_feedback('Finally found some who loves games as much as me', Raj, Zoe)
    add_feedback('Will be seeing you again for dinner I hope', Blair, Amy)
    add_feedback('Was shite since test doesnt even exist', test, Amy)

    # Execute the matchmaking algorithm
    magic(request=None)

# Start execution here!
if __name__ == '__main__':
    print "Starting LunchUp population script..."
    populate()