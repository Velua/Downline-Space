from django.conf.urls import url, include
from django.contrib import admin


from .views import list_mobileservices, create_mobileservice, create_electricityservice, create_broadbandservice, create_securityservice, create_phoneservice


urlpatterns = [
	url(r'^mobile/create/(?P<cust>\d+)/', create_mobileservice, name='create_mobileservice'),
	url(r'^mobile/', list_mobileservices, name='list_mobileservices'),
	url(r'^electricity/create/(?P<cust>\d+)/', create_electricityservice, name='create_electricityservice'),
	url(r'^mobilebroadband/create/(?P<cust>\d+)/', create_broadbandservice, name='create_broadbandservice'),
	url(r'^security/create/(?P<cust>\d+)/', create_securityservice, name='create_securityservice'),
	url(r'^phone/create/(?P<cust>\d+)/', create_phoneservice, name='create_phoneservice'),

]
