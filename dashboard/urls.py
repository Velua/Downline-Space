from django.conf.urls import url, include
from django.contrib import admin


from .views import profile_home

urlpatterns = [
	url(r'^$', profile_home, name='profile_home'),

]
