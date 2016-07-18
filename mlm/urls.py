from django.conf.urls import url, include
from django.contrib import admin


from .views import list_members, create_person, list_persons, detail_member, detail_person, create_member, create_activity, update_member, friendscsvupload, delete_person
from dashboard.views import importfacebookfriends

urlpatterns = [
	url(r'^activity/create/(?P<id>\d+)/', create_activity, name='create_activity'),
	url(r'^persons/create', create_person, name='create_person'),
	url(r'^members/create', create_member, name='create_member'),
	url(r'^activity/delete/(?P<id>\d+)/', delete_person, name='delete_person'),
	url(r'^members/', list_members, name='list_members'),
	url(r'^members/(?P<username>\d+)/', detail_member, name='detail_member'),
	url(r'^member/update', update_member, name='update_member'),
	url(r'^facebookfriends/upload', importfacebookfriends, name='importfacebookfriends'),
	url(r'^a', friendscsvupload, name='friendscsvupload'),











	url(r'^persons/', list_persons, name='list_persons'),
	

]
