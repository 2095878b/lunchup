from django.test import TestCase

from main.models import University, UserProfile, Feedback, Notification, TimeInterval
from django.core.urlresolvers import reverse

class UniversityMethodTests(TestCase):

    def test_that_it_is_Glasgow_uni(self):

        uni = University(domain="gla.ac.uk")
        uni.save()
        self.assertEqual((uni.domain == "gla.ac.uk"), True)

class UserProfileTests(TestCase):

    def check_person_is_from_glasgow(self):

        prof = UserProfile(user='sam', fullName = 'Samantha Jones', publicEmail="lalasam@gmail.com",
                            interests = '', about="")
        prof.save
        self.assertEqual((prof.university == "Glasgow"), True)

class TimeIntervalTests(TestCase):

    def check_day_is_a_day(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        new_day = TimeInterval(time=14, day="Monday")
        self.assertIn(new_day.day,days,True)


class
# Create your tests here.
