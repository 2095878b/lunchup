from django.db import models
from django.contrib.auth.models import User

# TODO: check foreign key on_delete parameter (low priority, later on)

class Interest(models.Model):
    name = models.CharField(max_length=64)

class University(models.Model):
    domain = models.CharField(max_length=64)

    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        verbose_name_plural = "universities"

class UserProfile(models.Model):
    # TODO: Check the constraints
    user = models.OneToOneField(User)
    fullName = models.CharField(max_length=64)
    publicEmail = models.EmailField()

    interests = models.ManyToManyField(Interest)

    # Can be blank/null for now
    university = models.ForeignKey(University, blank=True, null=True)
    about = models.TextField(max_length=6000)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    birthday = models.DateField(blank=True, null=True)

class Lunch(models.Model):
    # TODO: Consider renaming these two
    userOne = models.ForeignKey(User, related_name='uone')
    userTwo = models.ForeignKey(User, related_name='utwo')
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "lunches"

class Feedback(models.Model):
    content = models.CharField(max_length=6000)
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
    time = models.TimeField()
    day = models.PositiveSmallIntegerField()

#class Message(models.Model):
#    content = models.CharField(max_length=6000)
#    author = models.ForeignKey(User, related_name='message_author')
#    recipient = models.ForeignKey(User, related_name='message_recipient')
#    time = models.DateTimeField()
    # TODO: excluded boolean isMessageRead, implement later

class Notification(models.Model):
    userOne = models.ForeignKey(User, related_name='userone')
    userTwo = models.ForeignKey(User, related_name='usertwo')
    acceptedOne = models.BooleanField(default=False)
    acceptedTwo = models.BooleanField(default=False)
    available = models.DateTimeField()