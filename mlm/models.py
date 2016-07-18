from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.





TT = "Team Trainer"
QTT = "Qualified Team Trainer"
ETT = "Executive Team Trainer"
ETL = "Executive Team Leader"
TC = "Team Coordinator"
RD = "Regional Director"
RVP = "Regional Vice President"
SVP = "Senior Vice President"

positions = [
	(TT, "Team Trainer"),
	(QTT, "Qualified Team Trainer"),
	(ETT, "Executive Team Trainer"),
	(ETL, "Executive Team Leader"),
	(TC, "Team Coordinator"),
	(RD, "Regional Director"),
	(RVP, "Regional Vice President"),
	(SVP, "Senior Vice President"),
	

]



class Team(models.Model):
	name = models.CharField(max_length=64,blank=False,null=False)
	established = models.DateField(auto_now=False,auto_now_add=False,null=False)



M = "M"
F = "F"

genders = [

	(M, "Male"),
	(F, "Female"),
	
	]

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=32,default="",verbose_name="First name")
	lastname = models.CharField(max_length=32,default="",verbose_name="Last name")
	gender = models.CharField(max_length=1,choices=genders,default=M)
	birthday = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
	businessid = models.CharField(max_length=10,verbose_name="Business ID #")
	customerpoints = models.IntegerField(null=True,blank=True,verbose_name="Customer Points")
	position = models.CharField(choices=positions,max_length=32,verbose_name="Position")
	team = models.ForeignKey(Team,null=True,blank=True)



	def __unicode__(self):
		return str(self.user)



	
	
	def __unicode__(self):
		return self.firstname + " " + self.lastname

call = "Call"
bom = "Business Opportunity Meeting"
onetoten = "One To Ten"
meeting = "Meeting"

typeofactivitys = [

	(call, "Call"),
	(bom, "Business Opportunity Meeting"),
	(onetoten, "One To Ten"),
	(meeting, "Meeting"),
]



Lead = "Lead"
Customer = "Customer"
Prospect = "Prospect"

statuss = [
	(Lead, "Lead"),
	(Customer, "Customer"),
	(Prospect, "Prospect"),
]


QLD = "QLD"
NSW = "NSW"
WA = "WA"
SA = "SA"
TAS = "TAS"
VIC = "VIC"


states = [
	(QLD, "QLD"),
	(NSW, "NSW"),
	(WA, "WA"),
	(SA, "SA"),
	(TAS, "TAS"),
	(VIC, "VIC")
]




class Person(models.Model):
	owner = models.ForeignKey(Member,null=True)
	name = models.CharField(max_length=84,null=False)
	status = models.CharField(max_length=100,choices=statuss,null=False,blank=False)
	mobile = models.CharField(max_length=16,null=True,blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	facebooklink = models.CharField(max_length=128,null=True,blank=True,verbose_name="Facebook profile link")
	birthday = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
	gender = models.CharField(max_length=1,choices=genders,null=True,blank=True)
	streetno = models.CharField(max_length=12,null=True,blank=True,verbose_name="Street #")
	streetaddress = models.CharField(max_length=64,null=True,blank=True,verbose_name="Street")
	suburb = models.CharField(max_length=32,null=True,blank=True,verbose_name="Suburb/City")
	state = models.CharField(max_length=32,choices=states,null=True,blank=True,verbose_name="State")
	postcode = models.CharField(max_length=8,blank=True,null=True)
	notes = models.TextField(max_length=1024,null=True,blank=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)

	def __unicode__(self):
		return self.name
	
	

class Activity(models.Model):
	person = models.ForeignKey(Person)
	typeofactivity = models.CharField(choices=typeofactivitys,max_length=64)
	notes = models.TextField(max_length=2096,null=True,blank=True)
	timeofactivity = models.TimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
	dateofactivity = models.DateField(auto_now=False,auto_now_add=False,null=True,blank=True)
	dateandtime = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)

	def __unicode__(self):
		return self.typeofactivity + " with " + str(self.person)



class FriendCSVUpload(models.Model):
	friendscsvfile = models.FileField(null=True,blank=False,verbose_name="CSV File from PDF")
	member = models.ForeignKey(Member,null=True,blank=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)