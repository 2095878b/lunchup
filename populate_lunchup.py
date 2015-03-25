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

def add_user_profile(user, fullname, email, about, interests, picture):
    p = UserProfile.objects.get_or_create(user=user, fullName=fullname,
                                          publicEmail=email, about=about, interests=interests, picture=picture)[0]
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
                                           acceptedOne=accepted1, acceptedTwo=accepted2)[0]
    return n


#def add_interest(name):
#    i = Interest.objects.get_or_create(name=name)[0]
#    return i


def populate():
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
    glasgow = add_university(university='Glasgow University')

    # Add notifications
    omju = add_notification(om, ju, True,True)
    omju.available.add(sat13)
    amom = add_notification(om, am,True,True)
    amom.available.add(fri14)
    juam = add_notification(ju, am, True, True)
    juam.available.add(wed15)

    # Users
    om = add_user('omar', '2098877q@student.gla.ac.uk', 'root')
    om.save()
    ju = add_user('eust', '2095666e@student.gla.ac.uk', 'root')
    ju.save()
    am = add_user('amyx', '2195152a@student.gla.ac.uk', 'root')
    am.save()
    ra = add_user('vj', '2080123v@student.gla.ac.uk', 'root')
    ra.save()
    bl = add_user_profile('bliatch', '2078910A@student.gla.ac.uk', 'root')
    bl.save()
    zo = add_user('zoes', '2065610s@student.gla.ac.uk', 'root'  )
    zo.save()
    # User profiles
    Omar = add_user_profile(om, 'Omar Tufail', 'omar@gmail.com',
                            'about me', 'Going out, playing foodball, reading.', 'profile_images/omar.jpg')

    Omar.university = glasgow
    Omar.availability.add(sat13)
    Omar.availability.add(fri14)
    Omar.availability.add(wed15)
    Omar.save()

    Justas = add_user_profile(ju, 'Justas Bikulcius', 'eustace@yahoo.com',
                              'about me', 'Attending lectures, not doing drugs.', 'profile_images/justas.jpg')

    Justas.university = glasgow
    Justas.availability.add(sat13)
    Justas.availability.add(wed15)
    Justas.availability.add(tue13)
    Justas.save()

    Amy = add_user_profile(am, 'Amy Rose', 'xamyrosexx@aol.co.uk', 'about me', 'Listening to music and dancing.',
                           'profile_images/amy.jpg')

    Amy.availability.add(wed15)
    Amy.availability.add(fri14)
    Amy.availability.add(thu16)
    Amy.university = glasgow
    Amy.save()

    Raj = add_user_profile(ra, 'Rajeevan Vijayakumar', 'vj96@live.co.uk', 'about me', 'Playing games and reking noobs.',
                           'profile_images/raj.jpg' )

    Raj.university = glasgow
    Raj.availability.add(sat13)
    Raj.availability.add(thu16)
    Raj.availability.add(tue13)
    Raj.save()

    Blair = add_user_profile(bl, 'Blair Aitcheson', 'baitch96@hotmail.co.uk', 'about me', 'Listening to music and chilling',
                             'profile_images/blair.jpg' )

    Blair.university = glasgow
    Blair.availability.add(fri14)
    Blair.availability.add(wed15)
    Blair.availability.add(thu15)
    Blair.save()

    Zoe = add_user_profile(zo, 'Zoe Thorn', 'zzthorn@live.co.uk', 'about me', 'Watching Movies and going out',
                             'profile_images/zoe.jpg' )

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
# Start execution here!
if __name__ == '__main__':
    print "Starting LunchUp population script..."
    populate()