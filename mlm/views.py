from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from datetime import timedelta
from datetime import datetime

from .models import Member, Person, Activity
from services.models import MobileService, BroadbandService, SecurityService, ElectricityService, PhoneService
from django.contrib.auth.decorators import login_required


from dashboard.views import profile_home
from .forms import PersonForm, MemberForm, ActivityForm, FriendCSVUploadForm

# import necessary Django stuff
from django.http import HttpResponse

# import the wonderful decorator
from djstripe.decorators import subscription_payment_required

import requests


# @subscription_payment_required
@login_required
def create_member(request):

	form = MemberForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		requestinguser = request.user
		instance.user = requestinguser
		instance.save()
		return redirect(profile_home)





	context = {
		"title" : "Let's get started!",
		"notes" : "Enter your user & IBO information",

		"form" : form,
	}
	return render(request, "create_form.html", context)

# @subscription_payment_required
@login_required
def list_members(request):

	queryset = Member.objects.all()

	context = {

	"members" : queryset,

	}


	return render(request, "list_members.html", context)


# @subscription_payment_required
@login_required
def detail_member(request,username=None):

	member = get_object_or_404(Member,username=username)

	context = {

		"member" : member,
	}

	return render(request, "detail_member.html", context)

# @subscription_payment_required
@login_required
def detail_person(request,id=None):

	person = get_object_or_404(Person,id=id)


	mobileservices = MobileService.objects.filter(customer=person)
	activitys = Activity.objects.filter(person=person)
	activitycount = len(activitys)
	broadbandservices = BroadbandService.objects.filter(customer=person)
	securityservices = SecurityService.objects.filter(customer=person)
	electricityservices = ElectricityService.objects.filter(customer=person)
	phoneservices = PhoneService.objects.filter(customer=person)

	print "*****"
	print activitys
	print "*****"

	servicescount = len(mobileservices) + len(broadbandservices)
	context = {
		"activitys" : activitys,
		"person" : person,
		"mobileservices" : mobileservices,
		"servicescount" : servicescount,
		"activitycount" : activitycount,
		"broadbandservices" : broadbandservices,
		"securityservices" : securityservices,
		"electricityservices" : electricityservices,
		"phoneservices" : phoneservices,
	}

	return render(request, "detail_person.html", context)




# @subscription_payment_required
@login_required
def delete_person(request,id=None):

	person = get_object_or_404(Person,id=id)
	person.delete()

	return redirect('list_persons')




from allauth.socialaccount.models import SocialAccount, SocialToken

# @subscription_payment_required
# @login_required
# def list_persons(request):
	
# 	fbid = SocialAccount.objects.filter(user=request.user,provider="facebook").first()

# 	social_token = SocialToken.objects.filter(account__user=request.user, account__provider="facebook").first()

# 	requestinguser = request.user
# 	memberobj = Member.objects.filter(user__username=requestinguser)[0]

	# uid = fbid.uid
	# token = social_token.token
	# print token
	# print uid
	# # SubwaySandwich.objects.filter(train__id=id)

	# base_url = "https://graph.facebook.com/v2.3/"
	# limit = "900"
	# basicreq = "{base_url}{uid}/taggable_friends?access_token={token}&limit={limit}&format=json".format(base_url=base_url,uid=uid,token=token,limit=limit)

	# r = requests.get(basicreq)
	# print r.status_code

	# """
	# import json

	# json_data = json.loads(r.text)
	# print type(json_data)
	# print list(json_data.keys())

	# print "The request URL is.. "
	# print basicreq

	# # print "Returned data.."
	# # print json_data

	# print r.json()['paging']

	# """

	# import pprint
	# json_data = r.json()

	# pprint.pprint(json_data)

	# print ''
	# print ''

	# for data_thing in json_data['data']:
	# 	name = data_thing['name']
	# 	friendid = data_thing['id']
	# 	#do something with name ...
	# 	tmp = Person.objects.create()
	# 	tmp.owner = memberobj
	# 	tmp.firstname = name
	# 	tmp.lastname = "."
	# 	tmp.status = "Lead"
	# 	tmp.mobile = "N/A"
	# 	tmp.save()

	# 	print name
	# 	print friendid
	# 	print ""




# 	requestinguser = request.user
# 	memberobj = Member.objects.filter(user__username=requestinguser)

# 	queryset = Person.objects.filter(owner=memberobj)

# 	context = {

# 	"persons" : queryset,

# 	}

# 	return render(request, "list_personss.html", context)



# @subscription_payment_required
@login_required
def list_persons(request):
	
	requestinguser = request.user


	memberobj = Member.objects.filter(user__username=requestinguser)

	if not memberobj:
		return redirect('create_member')

	requestinguser = request.user
	memberobj = Member.objects.filter(user__username=requestinguser)[0]


	queryset = Person.objects.filter(owner=memberobj).order_by('name')

	context = {

	"persons" : queryset,

	}

	return render(request, "list_personss.html", context)





# @subscription_payment_required
@login_required
def update_person(request, id=None):

	person = get_object_or_404(Person,id=id)
	mobileservices = MobileService.objects.filter(customer=person)

	form = PersonForm(request.POST or None,instance=person)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect(detail_person, id=person.id)


	context = {
		"title" : "Update contact",
		"notes" : "Update contact information.",

		"person" : person,
		"services" : mobileservices,
		"form" : form,
	}

	return render(request, "create_form.html", context)



# @subscription_payment_required
@login_required
def create_person(request):

	form = PersonForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		requestinguser = request.user
		memberobj = Member.objects.filter(user__username=requestinguser)[0]
		instance.owner = memberobj
		instance.save()
		return redirect(list_persons)

	context = {
		"title" : "New contact",
		"notes" : "Create your new contact",

		"form" : form,
	}
	return render(request, "create_form.html", context)


# @subscription_payment_required
@login_required
def create_activity(request,id=None):

	form = ActivityForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		personobj = Person.objects.filter(id=id)[0]
		instance.person = personobj
		instance.dateandtime = datetime.combine(instance.dateofactivity, instance.timeofactivity)
		instance.save()
		return redirect(detail_person, id=personobj.id)

	context = {
		"title" : "New activity",
		"notes" : "Log new activity",
		"form" : form,
	}
	return render(request, "create_form.html", context)





# @subscription_payment_required
@login_required
def update_member(request, id=None):

	requestinguser = request.user
	memberobj = Member.objects.filter(user__username=requestinguser)[0]


	form = MemberForm(request.POST or None,instance=memberobj)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect(profile_home)


	context = {
		"title" : "Update your information",
		"notes" : "Update your IBO information.",
		"form" : form,
	}

	return render(request, "create_form.html", context)



from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def friendscsvupload(request):


	form = FriendCSVUploadForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		DatFile = instance
		s = str(DatFile.friendscsvfile.url)
		s = s
		x = s
		print s
		print x
		print "*****"




		# f = open(DatFile.csvfile.url,'r')
		f = requests.get(x, stream=True).raw
		#f = open(x,'r')
		##f.next()
		try:	
			for line in f:
				line =  line.split(',')
				tmp = Person.objects.create()
				tmp.owner = instance.member
				tmp.name = line[0]
				tmp.status = "Lead"
				tmp.save()
		finally:
			f.close()



	context = {
		"title" : "New activity",
		"notes" : "Log new activity",
		"form" : form,
	}
	return render(request, "create_csv.html", context)