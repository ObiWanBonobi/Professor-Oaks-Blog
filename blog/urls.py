""" Urls for blog page, connects to the PostList class in the views.py file """

from django.urls import path
from . import views


urlpatterns = [path('', views.PostList.as_view(), name='home'),]
path('<slug:slug>/', views.post_detail, name='post_detail'),
