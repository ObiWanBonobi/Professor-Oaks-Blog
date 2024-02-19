""" URL configuration for profoak project """

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('database/', include('database.urls'), name='database-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('user_profile/', include('user_profile.urls'), name='profile-urls'),
    path('', include('blog.urls'), name='blog-urls'),
]
