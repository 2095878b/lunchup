from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    name = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)

    def __unicode__(self):
        return u'%s' % self.name
    class Meta:
        verbose_name_plural = "universities"

class TimeInterval(models.Model):
    time = models.PositiveSmallIntegerField()
    day = models.CharField(max_length=10)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullName = models.CharField(max_length=64)
    publicEmail = models.EmailField()
    availability = models.ManyToManyField(TimeInterval)

    interests = models.CharField(max_length=250)

    university = models.ForeignKey(University, blank=True, null=True)
    about = models.TextField(max_length=6000)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):

        domain = self.user.email.split('@')[1]
        found = False
        for uni in University.objects.all():
            if uni.domain in domain:
                self.university = uni
                break
        super(UserProfile, self).save(*args, **kwargs)

class Feedback(models.Model):
    content = models.CharField(max_length=6000)
    recipient = models.ForeignKey(UserProfile, related_name='feedback_recipient')
    author = models.ForeignKey(UserProfile, related_name='feedback_author')

    class Meta:
        verbose_name_plural = "feedback"

class Notification(models.Model):
    userOne = models.ForeignKey(UserProfile, related_name='userone')
    userTwo = models.ForeignKey(UserProfile, related_name='usertwo')
    acceptedOne = models.BooleanField(default=False)
    acceptedTwo = models.BooleanField(default=False)
    available = models.ManyToManyField(TimeInterval)