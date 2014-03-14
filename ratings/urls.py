try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

urlpatterns = patterns('ratings.views',
    url(r'^vote/$', 'vote', name='ratings_vote'),
)
