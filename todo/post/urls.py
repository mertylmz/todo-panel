from django.conf.urls import url
from django.contrib import admin
from home.views import home_view
from .views import *


app_name = 'post'


urlpatterns = [

    url(r'^index$', post_index, name='index'),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^create$', post_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete$', post_delete, name='delete'),
    url(r'^(?P<ids>(\d+,)+\d+)/personel/$', post_personel, name='personel'),
    url(r'^(?P<ids>\d+)/personel/$', post_personel, name='personel'),
    url(r'^(?P<id>\d+)/personel_ajax/$', post_personel_ajax, name='personel_ajax'),
    url(r'^(?P<id>\d+)/home_view$', home_view, name='home'),

]