from django.conf.urls import patterns, include, url
from django.contrib import admin
from lunchup import settings
from registration.backends.simple.views import RegistrationView
<<<<<<< HEAD
=======

>>>>>>> ede1509d0cd9e3491d4689d50287e649549bffea

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/'

urlpatterns = patterns('',
    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
<<<<<<< HEAD
    # url(r'^ajaximage/', include('ajaximage.urls')),
=======
>>>>>>> ede1509d0cd9e3491d4689d50287e649549bffea
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
