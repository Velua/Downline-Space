from django.shortcuts import render, redirect

# Create your views here.

from .models import MobileService, ElectricityService, BroadbandService, PhoneService
from mlm.views import list_persons, detail_person
from .forms import MobileServiceForm, ElectricityServiceForm, BroadbandServiceForm, SecurityServiceForm, PhoneServiceForm

from mlm.models import Member, Person

def list_mobileservices(request):

	queryset = MobileService.objects.all()

	context = {

	"mobileservices" : queryset,

	}

	return render(request, 'list_mobileservices.html', context)




def create_mobileservice(request,cust=None):

	form = MobileServiceForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		requestinguser = request.user
		memberobj = Member.objects.filter(user__username=requestinguser)[0]
		customerobj = Person.objects.filter(id=cust)[0]
		instance.customer = customerobj
		instance.owner = memberobj
		instance.save()
		return redirect(detail_person, id=customerobj.id)
	context = {
		"name" : str(cust),
		"title" : "New Mobile Service",
		"notes" : "Enter mobile service information to know when to follow up!",
		"form" : form,
	}

	return render(request, "create_form.html", context)

def create_electricityservice(request,cust=None):

	form = ElectricityServiceForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		requestinguser = request.user
		memberobj = Member.objects.filter(user__username=requestinguser)[0]
		customerobj = Person.objects.filter(id=cust)[0]
		instance.customer = customerobj
		instance.owner = memberobj
		instance.save()
		return redirect(detail_person, id=customerobj.id)

	context = {
		"name" : str(cust),
		"title" : "New Electricity Service",
		"notes" : "Enter electricity service information to know when to follow up!",
		"form" : form,
	}

	return render(request, "create_form.html", context)


def create_broadbandservice(request,cust=None):

	form = BroadbandServiceForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		requestinguser = request.user
		memberobj = Member.objects.filter(user__username=requestinguser)[0]
		customerobj = Person.objects.filter(id=cust)[0]
		instance.customer = customerobj
		instance.owner = memberobj
		instance.save()
		return redirect(detail_person, id=customerobj.id)

	context = {
		"name" : str(cust),
		"title" : "New Broadband Service",
		"notes" : "Enter Broadband service information to know when to follow up!",
		"form" : form,
	}

	return render(request, "create_form.html", context)





def create_securityservice(request,cust=None):

	form = SecurityServiceForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		requestinguser = request.user
		memberobj = Member.objects.filter(user__username=requestinguser)[0]
		customerobj = Person.objects.filter(id=cust)[0]
		instance.customer = customerobj
		instance.owner = memberobj
		instance.save()
		return redirect(detail_person, id=customerobj.id)

	context = {
		"name" : str(cust),
		"title" : "New Security Service",
		"notes" : "Enter Security service information to know when to follow up!",
		"form" : form,
	}

	return render(request, "create_form.html", context)



def create_phoneservice(request,cust=None):

	form = PhoneServiceForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		requestinguser = request.user
		memberobj = Member.objects.filter(user__username=requestinguser)[0]
		customerobj = Person.objects.filter(id=cust)[0]
		instance.customer = customerobj
		instance.owner = memberobj
		instance.save()
		return redirect(detail_person, id=customerobj.id)

	context = {
		"name" : str(cust),
		"title" : "New Phone Service",
		"notes" : "Enter Phone service information to know when to follow up!",
		"form" : form,
	}

	return render(request, "create_form.html", context)