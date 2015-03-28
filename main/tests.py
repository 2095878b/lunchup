from django.test import TestCase, Client

from main.models import *
from main.views import magic
from django.core.urlresolvers import reverse

class UniversityMethodTests(TestCase):

    def test_new_university(self):

        uni = University(domain="random.edu", name="random")
        uni.save()
        self.assertEqual((uni.domain == "random.edu"), True)
        self.assertEqual((uni.name == "random"), True)

class UserProfileTests(TestCase):

    def test_check_email_is_parsed_and_uni_is_set(self):

        sam = User.objects.create_user('sammy6', '2095871k@staff.gla.ac.uk', 'nyannyan')
        prof = UserProfile(user=sam, fullName = 'Samantha Jones', publicEmail="lalasam@gmail.com",
                            interests = 'Sleeping', about="Nothing much")
        prof.save()
        uni = University.objects.get_or_create(name="Glasgow", domain="gla.ac.uk")
        self.assertEqual((prof.university == uni), True)

class TimeIntervalTests(TestCase):

    def test_check_if_info_set_correct(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        new_day = TimeInterval(time=14, day="Monday")
        self.assertIn(new_day.day, days, True)
        self.assertEqual(new_day.time, 14)

class NotificationTests(TestCase):

    def test_page_displays_no_matches(self):

        c = Client()
        print c.login(username='amyx', password='root')
        response = self.client.get(reverse('notifications'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('No notifications yet.', response.content)

    def setup(self):
        dave = UserProfile.objects.get_or_create(user = 'dave', fullName = 'Dave Smith', publicEmail="something@student.gla.ac.uk", interests='', about='')
        steve = UserProfile.objects.get_or_create(user = 'steve', fullName = 'Steve Smith', publicEmail="somethingelse@student.gla.ac.uk", interests='', about='')

        timeSlot = TimeInterval.obects.get_or_create(time=13, day="Tuesday")

        dave.availability = timeSlot
        steve.availability = timeSlot

        magic()

    def test_notifications_are_working(self):

        response = self.client.get(reverse('notifications'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(response.content, 'No notifications yet')
