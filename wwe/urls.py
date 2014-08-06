from django.conf.urls import patterns, include, url
from django.contrib import admin
from players.views import home

urlpatterns = patterns('',
    url(r'^$', 'players.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/$', 'players.views.create'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^players/', include('players.urls')),
    url(r'^accounts/login/$', 'wwe.views.login'),
    url(r'^accounts/auth/$', 'wwe.views.auth_view'),
    #url(r'^accounts/logout/$', 'wwe.views.logout'),
    url(r'^accounts/loggedin/$', 'wwe.views.loggedin'),
    #url(r'^accounts/invalid/$', 'wwe.views.invalid_login'),
    url(r'^accounts/register/$', 'wwe.views.register_user'),
    url(r'^accounts/register_success/$', 'wwe.views.register_success'),
    url(r'^search/$', 'players.views.search_new')
)
