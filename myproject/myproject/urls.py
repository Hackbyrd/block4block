from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myproject.views.home', name = 'home'),
    url(r'^mochi.html$', 'myproject.views.mochi', name = 'mochi'),
    url(r'^addgame$', 'games.views.addGame', name = 'addGame'),
    url(r'^(?P<game_id>\d+)/$', 'games.views.game', name = 'game'),
    url(r'^search$', 'myproject.views.search', name = 'search'),
    url(r'^search/(?P<category>\w+)/$', 'myproject.views.search_scroll', name = 'search_scroll'),
    #url(r'^search/(?P<page>\d+)$', 'myproject.views.search', name = 'search'),
    #url(r'^search/(?P<category>\w+)/(?P<page>\d+)$', 'myproject.views.nextPage', name = 'nextPage'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
