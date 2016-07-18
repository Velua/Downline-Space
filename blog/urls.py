from django.conf.urls import url, include
from django.contrib import admin

from .views import blog_list

urlpatterns = [
	url(r'^$', blog_list, name='blog_list'),

]
