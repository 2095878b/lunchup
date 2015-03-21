from django.conf.urls import patterns, include, url
from django.contrib import admin
from lunchup import settings
from registration.backends.simple.views import RegistrationView
from main.api import UserProfileResource, InterestResource
from tastypie.api import Api


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/edit_profile/'

v1_api = Api(api_name='v1')
v1_api.register(InterestResource())
v1_api.register(UserProfileResource())

urlpatterns = patterns('',
    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )