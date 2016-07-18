from django.shortcuts import render, redirect

import datetime
from datetime import timedelta
from django.utils import timezone
from django.db import models
import time

# Create your views here.

from services.models import MobileService
from mlm.models import Member, Person
from .models import Quote
from .forms import FacebookFriendsForm

# import necessary Django stuff
from django.http import HttpResponse

# import the wonderful decorator
from djstripe.decorators import subscription_payment_required



def profile_home(request):
	if not request.user.is_authenticated():
		return render(request, "index.html")
	requestinguser = request.user


	memberobj = Member.objects.filter(user__username=requestinguser).first()


	if not memberobj:
		return redirect('create_member')
	

	persons = Person.objects.filter(owner=memberobj)
	print persons


	startdate = datetime.date.today()
	enddate = startdate + timedelta(days=30)



	nearmobileservices = []

	for person in persons:
		obj = MobileService.objects.filter(customer=person,expiry__range=[startdate, enddate])
		if obj:
			nearmobileservices.append(obj)
	#nearmobileservices = MobileService.objects.filter(customer=persons,expiry__range=[startdate, enddate])


	totalmobileservices = []
	for person in persons:
		obj = MobileService.objects.filter(customer=person)
		for svc in obj:
			totalmobileservices.append(obj)
	totalmobileservices = len(totalmobileservices)


	quote = Quote.objects.order_by('?').first()


	personstotal = len(persons)
	possibleservices = personstotal * 5



	nomobile = 0
	for person in persons: 
		obj = MobileService.objects.filter(customer=person)
		if not obj:
			nomobile += 1

	print "No mobile is "
	print nomobile


	context = {
	"nomobile" : nomobile,

	"personstotal" : personstotal,
	"services" : nearmobileservices,
	"quote" : quote,
	"member" : memberobj,
	"possibleservices" : possibleservices,
	"totalmobileservices" : totalmobileservices,

	}

	return render(request, "luna/index.html", context)


from mlm.models import Person
# from .forms import CSVForm
from time import sleep

def import_csv(request):
	if not request.user.is_authenticated():
		return render(request, "index.html")

	requestinguser = request.user
	memberobj = Member.objects.filter(user__username=requestinguser)[0]

	if not memberobj:
		return redirect('create_member')

	form = CSVForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		DatFile = instance
		s = str(DatFile.csvfile.url)
		x = s[1:]
		print s
		print x
		print "*****"
		sleep(3.0) # Time in seconds.

		# f = open(DatFile.csvfile.url,'r')
		f = open(x,'r')
		f.next()
		try:	
			for line in f:
				line =  line.split(',')
				tmp = Person.objects.create()
				tmp.owner = memberobj
				tmp.firstname = line[0]
				tmp.lastname = line[1]
				tmp.status = "Lead"
				tmp.mobile = line[2]
				tmp.save()
		finally:
			f.close()



	context = {
		"title" : "New activity",
		"notes" : "Log new activity",
		"form" : form,
	}
	return render(request, "create_csv.html", context)


def import_csv(request):
	if not request.user.is_authenticated():
		return render(request, "index.html")

	requestinguser = request.user
	memberobj = Member.objects.filter(user__username=requestinguser)[0]

	if not memberobj:
		return redirect('create_member')

	form = CSVForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		DatFile = instance
		s = str(DatFile.csvfile.url)
		x = s[1:]
		print s
		print x
		print "*****"
		sleep(3.0) # Time in seconds.

		# f = open(DatFile.csvfile.url,'r')
		f = open(x,'r')
		f.next()
		try:	
			for line in f:
				line =  line.split(',')
				tmp = Person.objects.create()
				tmp.owner = memberobj
				tmp.firstname = line[0]
				tmp.lastname = line[1]
				tmp.status = "Lead"
				tmp.mobile = line[2]
				tmp.save()
		finally:
			f.close()



	context = {
		"title" : "New activity",
		"notes" : "Log new activity",
		"form" : form,
	}
	return render(request, "create_csv.html", context)




from django.conf import settings
from django.core.mail import send_mail




def importfacebookfriends(request):
	if not request.user.is_authenticated():
		return render(request, "index.html")

	requestinguser = request.user
	memberobj = Member.objects.filter(user__username=requestinguser)[0]

	if not memberobj:
		return redirect('create_member')

	form = FacebookFriendsForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.member = memberobj
		instance.save()
		DatFile = instance
		s = str(DatFile.friendsfile.url)
		send_mail("New Facebook friends upload!", "Someone has uploaded a new file! Get on it!", settings.EMAIL_MAIN, ["john@empire.systems"], fail_silently=False)
		return redirect(profile_home)
	context = {
		"title" : "Import Facebook Friends!",
		"notes" : "Upload document containing your friends names & we'll put them in your contacts!",
		"form" : form,
	}
	return render(request, "importfacebookfriends.html", context)



