from django import forms


from .models import Person, Member, Activity, FriendCSVUpload
from django.contrib.admin import widgets                                       



class DateInput(forms.DateTimeInput):
    input_type = 'date'
 
class TimeInput(forms.DateTimeInput):
    input_type = 'time'


class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = [

		"name",
		"status",
		"mobile",
		"email",
		"facebooklink",
		"birthday",
		"gender",
		"streetno",
		"streetaddress",
		"suburb",
		"state",
		"postcode",
		"notes",

		]


class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = [

		"firstname",
		"lastname",
		"businessid",
		"customerpoints",
		"position",

		"gender",
		"birthday",

		]
		widgets = {
            'birthday': DateInput(),
        }


class FriendCSVUploadForm(forms.ModelForm):
	class Meta:
		model = FriendCSVUpload
		fields = [
		"friendscsvfile",
		"member",
		]


class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity
		fields = [

		"typeofactivity",
		"notes",
		"timeofactivity",
		"dateofactivity",
		
		]
		widgets = {
            'timeofactivity': TimeInput(),
            'dateofactivity': DateInput(),
        }





