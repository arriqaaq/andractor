from django.conf.urls import patterns, url
from droid import views
urlpatterns = patterns('',
    url(r'^list/$', views.list, name='list'),
    url(r'^list/(?P<apkid>[\w\-]+)/$', views.permission, name='permission'),
)
