from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from mlm.models import Member



# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(Member,default=0,null=True)
	title = models.CharField(max_length=32,null=False,blank=False)
	content = models.TextField(max_length=4096,null=True,blank=True)
	image = models.FileField(null=True,blank=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)


	def __unicode__(self):
		return str(self.title)


