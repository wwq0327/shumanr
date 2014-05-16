from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'home.views.index'),
                       url(r'^logout/$', 'home.views.logout'),
)                       
