from django.db import models
from django.contrib.auth.models import User

# TODO: check foreign key on_delete parameter (low priority, later on)

class Interest(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

class University(models.Model):
    name = models.CharField(max_length=64)
    # TODO: Location, excluded for now

    class Meta:
        verbose_name_plural = "universities"

class UserProfile(models.Model):
    # TODO: Check the constraints
    user = models.OneToOneField(User)
    firstName = models.CharField(max_length=64)
    lastName = models.IntegerField(max_length=64)
    regularEmail = models.EmailField()

    interests = models.ManyToManyField(Interest)

    university = models.ForeignKey(University)
    degree = models.CharField(max_length=64)
    about = models.TextField(max_length=6000)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    birthday = models.DateField()

class Lunch(models.Model):
    # TODO: Consider renaming these two
    userOne = models.ForeignKey(User, related_name='userone')
    userTwo = models.ForeignKey(User, related_name='usertwo')
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "lunches"

class Feedback(models.Model):
    content = models.CharField(max_length=6000)
    # TODO: is a numerical rating needed?
    rating = models.PositiveSmallIntegerField()
    recipient = models.ForeignKey(User, related_name='feedback_recipient')
    author = models.ForeignKey(User, related_name='feedback_author')
    # Time when the feedback was left, not the lunch date
    time = models.DateTimeField()
    lunch = models.ForeignKey(Lunch)

    class Meta:
        verbose_name_plural = "feedback"

class TimeInterval(models.Model):
    user = models.ForeignKey(User)
    timeFrom = models.DateTimeField()
    timeTo = models.DateTimeField()

class Message(models.Model):
    content = models.CharField(max_length=6000)
    author = models.ForeignKey(User, related_name='message_author')
    recipient = models.ForeignKey(User, related_name='message_recipient')
    time = models.DateTimeField()
    # TODO: excluded boolean isMessageRead, implement later
