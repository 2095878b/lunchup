from django.conf.urls import patterns, url, include
from main import views

urlpatterns = patterns('',
    url(r'^$', views.splash, name='splash'),
    url(r'^how_it_works/$', views.how_it_works, name='how_it_works'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='myprofile'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^availability/$', views.avail, name='avail'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^upload_picture/$', views.upload_picture, name='upload_picture'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^get_avail/$', views.get_avail, name='get_avail'),
    url(r'^add_avail/$', views.add_avail, name='add_avail'),
    url(r'^rm_avail/$', views.rm_avail, name='rm_avail'),
    url(r'^accept_or_decline/$', views.accept_or_decline, name='accept_or_decline'),
    url(r'^magic/$', views.magic, name='magic'),
)