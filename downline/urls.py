"""downline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from mlm.views import detail_person, update_person
from dashboard.views import import_csv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^persons/update/(?P<id>\d+)/$', update_person, name='update_person'),
	url(r'^persons/(?P<id>\d+)/$', detail_person, name='detail_person'),
	url(r'^accounts/', include('allauth.urls')),
    url(r'^people/', include('mlm.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^payments/', include('djstripe.urls', namespace="djstripe")),
    url(r'^$', include('dashboard.urls')),
    url(r'^wtf/$', import_csv, name='import_csv'),

]
