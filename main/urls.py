from django.conf.urls import patterns, url, include
from main import views

urlpatterns = patterns('',
    url(r'^$', views.how_it_works, name = 'howitworks'),
    url(r'^splash/$', views.splash, name = 'splash'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^profile/$', views.profile, name='myprofile'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^availability/$', views.avail, name='avail'),
    url(r'^notifications/$', views.notifications, name='notifications'),
)