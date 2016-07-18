from __future__ import unicode_literals

from django.db import models

# Create your models here.


from mlm.models import Member

class Quote(models.Model):
	message = models.TextField(max_length=999,blank=False)
	speaker = models.CharField(max_length=140,blank=True,null=True)
	member = models.ForeignKey(Member,null=True,blank=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)


	def __unicode__(self):
		return str(self.message)


# class CSVUpload(models.Model):
# 	csvfile = models.FileField(null=True,blank=True)


class FacebookFriendUpload(models.Model):
	friendsfile = models.FileField(null=True,blank=False,verbose_name="PDF File")
	member = models.ForeignKey(Member,null=True,blank=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)

	def __unicode__(self):
		return str(self.member) + str(self.friendsfile)