import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lunchup.settings')

import django
django.setup()

from main.models import UserProfile, Interest, University, Lunch,
                        Feedback, Notification  

def populate():

    football = Interest(name='football')
	swimming = Interest(name='swimming')
	going_out = Interest(name='going out')
	reading = Interest(name='reading')
	
	glasgow = University(name='Glasgow University')

    Omar = add_userProfile('OmarT', 'Omar Tufail', 'Blah@blah.co.uk', 
	'about me', 'profile_images/omar.jpg')
	
	Omar.Interest.add(going_out)
	Omar.Interest.add(reading)
	Omar.University.add(glasgow)
	
	Justas = add_userProfile('xJustx', 'Justas Bikulcius', 'Blah2@blah.co.uk'
	'about me', 'profile_images/justas.jpg')
	
	Justas.Interest.add(going_out)
	Justas.Interest.add(football)
	Justas.University.add(glasgow)
	
	
	Amy = add_userProfile('amyxx', 'Amy Rose', 'Blah3@blah.co.uk','about me'
	, 'profile_images/amy.jpg')
	
	Amy.Interest.add(going_out)
	Amy.Interest.add(reading)
	Amy.University.add(glasgow)

   

    
def add_userProfile(user, fullName, email, about, picture):
    p = UserProfile.objects.get_or_create(user=user, fullName=fullName,
	    publicEmail=email, about=about, picture=picture)[0]
    return p

def add_feedback(content, rating, recipient, author, time, lunch):
    f = Feedback.objects.get_or_create(content=content,rating=rating
	recipient=recipient, author=author, time=time, lunch=lunch)[0]
    return f
	
def add_university(university):
    u = University.objects.get_or_create(domain=university)
	return u

def add_time(time,day):
    t = TimeInterval.objects.get_or_create(time=time, 
	day=day)
	return t
	
def add_nofification(user1, user2, accepted1,accepted2,available):
    n = Notification.objects.get_or_create(UserOne=user1, UserTwo=user1,
	acceptedOne=accepted1, acceptedTwo=accepted2, available=available)
    return n
def add_interest(name):
    i = Interest.objects.get_or_create(name=name)
	return i
	
def add_lunch(user1, user2, date):
    l = Lunch.objects.get_or_create(userOne=user1, userTwo=user2, date=date)
	return l
	
	
# Start execution here!
if __name__ == '__main__':
    print "Starting LunchUp population script..."
    populate()