"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import TweetListView,TweetDetailView,TweetCreateView
from .views import TweetDeleteView,tweet_update_view
from .views import post_create,post_detail,post_list
from .views import post_update,post_delete
from .views import TweetUpdateView,UserFormView
from .views import login_user,logout_user
from .views import TestCreateView,LoginUserView
from django.urls import re_path

app_name="tweets"


urlpatterns = [
  re_path(r'^$',TweetListView.as_view(),name='list'),
  re_path(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'),
  re_path(r'^create/$',TweetCreateView.as_view(),name='create'),
  # re_path(r'^(?P<pk>\d+)/$',tweet_detail_view,name='detail'),
  re_path(r'^test/$',TestCreateView.as_view(),name='create'),
  re_path(r'^(?P<pk>\d+)/update/$',TweetUpdateView.as_view(),name='update'),
  re_path(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(),name='delete'),  
  re_path(r'^post/create/$',post_create,name='postcreate'),   
  re_path(r'^post/(?P<id>\d+)/$',post_detail,name='postdetail'),
  re_path(r'^post/list/$',post_list,name='postlist'),
  re_path(r'^post/update/(?P<id>\d+)/$',post_update,name='postupdate'),
  re_path(r'^post/delete/(?P<id>\d+)/$',post_delete,name='postdelete'),
  re_path(r'^register/$',UserFormView.as_view(),name='register'),
  re_path(r'^login/$',LoginUserView.as_view(),name='login'),
  re_path(r'^login1/$',login_user,name='login1'),
  re_path(r'^logout/$',logout_user,name='logout'),

]
