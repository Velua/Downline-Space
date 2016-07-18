from __future__ import unicode_literals

from django.db import models

# Create your models here.

from mlm.models import Person


Optus = "Optus"
Telstra = "Telstra"
Amaysim = "Amaysim"
Vodafone  = "Vodafone"
Boost = "Boost"

mobileproviders = {
	(Optus, "Optus"),
	(Telstra, "Telstra"),
	(Amaysim, "Amaysim"),
	(Vodafone, "Vodafone"),
	(Boost, "Boost"),
}


Westnet = "Westnet"

broadbandproviders = {
	(Optus, "Optus"),
	(Telstra, "Telstra"),
	(Westnet, "Westnet"),
}

ADSL = "ADSL"
ADSL2 = "ADSL 2+"
NBN = "NBN"


connectiontypes = {
	(ADSL, "ADSL"),
	(ADSL2, "ADSL 2+"),
	(NBN, "NBN"),
}

iPhone = "iPhone"
Samsung = "Samsung"
HTC = "HTC"

phones = {
	(iPhone, "iPhone"),
	(Samsung, "Samsung"),
	(HTC, "HTC"),
}

Plan = "Plan"
Prepaid = "Prepaid"

servicetypes = {
	(Plan, "Plan"),
	(Prepaid, "Prepaid"),
}

class MobileService(models.Model):
	customer = models.ForeignKey(Person)
	provider = models.CharField(choices=mobileproviders,max_length=32,null=True,blank=False,default=Telstra)
	phone = models.CharField(choices=phones,max_length=32,null=True,blank=False,default=iPhone)
	servicetype = models.CharField(choices=servicetypes,max_length=32,null=True,blank=False,default="")
	monthlycost = models.FloatField(null=True,default=80,blank=True)
	expiry = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)

	def __unicode__(self):
		return str(self.customer) + "'s " + str(self.phone) + " $" + str(self.monthlycost) + " per month"


AGL = "AGL"
EnergyAustralia = "EnergyAustralia"
LumoEnergy = "LumoEnergy"
RedEnergy = "RedEnergy"
OriginEnergy = "OriginEnergy"


energyproviders = {
	(AGL, "AGL"),
	(EnergyAustralia, "EnergyAustralia"),
	(LumoEnergy, "LumoEnergy"),
	(RedEnergy, "RedEnergy"),
	(OriginEnergy, "OriginEnergy"),
}


class ElectricityService(models.Model):
	customer = models.ForeignKey(Person,default=0)
	provider = models.CharField(choices=energyproviders,max_length=64,null=True,blank=False,default=AGL)
	kwh = models.FloatField(null=True,default=0.5,blank=True)

	def __unicode__(self):
		return str(self.customer) + str(self.provider)


class BroadbandService(models.Model):
	customer = models.ForeignKey(Person,default=0)
	provider = models.CharField(choices=broadbandproviders,max_length=64,null=True,blank=True,default=Telstra)
	GBpermonth = models.IntegerField(null=True,blank=True)
	monthlycost = models.FloatField(null=True,default=80,blank=True,verbose_name="Monthly Cost")
	connectiontype = models.CharField(choices=connectiontypes,max_length=64,null=True,blank=True)
	expiry = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)


class SecurityService(models.Model):
	customer = models.ForeignKey(Person,default=0)
	interestedinsecuringhome = models.BooleanField(verbose_name="Interested in securing home")
	provider = models.CharField(max_length=64,null=True,blank=True,verbose_name="Provider")
	monthlycost = models.FloatField(null=True,default=80,blank=True,verbose_name="Monthly cost")
	expiry = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True,verbose_name="Expiry date of plan")


class PhoneService(models.Model):
	customer = models.ForeignKey(Person,default=0)
	provider = models.CharField(choices=broadbandproviders,max_length=64,null=True,blank=True,default=Telstra)
	monthlycost = models.FloatField(null=True,default=80,blank=True,verbose_name="Monthly Cost")
	expiry = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)

