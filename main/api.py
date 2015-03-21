from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from main.models import UserProfile, Interest

class InterestResource(ModelResource):
    class Meta:
        queryset = Interest.objects.all()
        resource_name = 'interest'

class UserProfileResource(ModelResource):
    #interest = fields.ManyToManyField(InterestResource, 'interest')
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'profile'
        authorization = Authorization()
        excludes = ['user', 'university']