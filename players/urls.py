from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/', 'players.views.players'),
    url(r'^get/(?P<player_id>\d+)/$', 'players.views.players_id'),
    url(r'^create/$', 'players.views.create'),
)
