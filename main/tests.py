from django.test import TestCase

from main.models import University, UserProfile, Feedback, Notification, TimeInterval
from main.views import magic
from django.core.urlresolvers import reverse

class UniversityMethodTests(TestCase):

    def test_that_it_is_Glasgow_uni(self):

        uni = University(domain="gla.ac.uk")
        uni.save()
        self.assertEqual((uni.domain == "gla.ac.uk"), True)

class UserProfileTests(TestCase):

    def test_check_person_is_from_glasgow(self):

        prof = UserProfile(user='sam', fullName = 'Samantha Jones', publicEmail="lalasam@gmail.com",
                            interests = '', about="")
        prof.save
        self.assertEqual((prof.university == "Glasgow"), True)

class TimeIntervalTests(TestCase):

    def test_check_day_is_a_day(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        new_day = TimeInterval(time=14, day="Monday")
        self.assertIn(new_day.day,days,True)

class NotificationTests(TestCase):

    def test_page_displays_no_matches(self):

        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response, 'No notifications yet.')

    def setup(self):
        dave = UserProfile.objects.get_or_create(user = 'dave', fullName = 'Dave Smith', publicEmail="something@student.gla.ac.uk", interests='', about='')
        steve = UserProfile.objects.get_or_create(user = 'steve', fullName = 'Steve Smith', publicEmail="somethingelse@student.gla.ac.uk", interests='', about='')

        timeSlot = TimeInterval.obects.get_or_create(time=13, day="Tuesday")

        dave.availability = timeSlot
        steve.availability = timeSlot

        magic()

    def test_notifications_are_working(self):
        
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(response, 'No notifications yet')
