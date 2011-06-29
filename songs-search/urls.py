from django.conf.urls.defaults import *
from django.conf import settings

handler500

urlpatterns = patterns('songs.songs-search.views',
url(r'^$', 'index', name="index"),
url(r'^search/$', 'search', name="search"),
)	

