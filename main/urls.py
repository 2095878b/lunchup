from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^splash/$', views.splash, name = 'splash'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^profile/$', views.profile, name='myprofile'),
    #url(r'^profile/(?P<category_name_slug>[\w\-]+)/add_page/$', views.profile, name='profile'),
    url(r'^availability/$', views.availability, name='availability'),
    url(r'^history/$', views.history, name='history'),
)