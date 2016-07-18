from django import forms
from django.forms import ModelForm

from .models import MobileService, ElectricityService, BroadbandService, SecurityService, PhoneService

class DateInput(forms.DateInput):
    input_type = 'date'


class MobileServiceForm(forms.ModelForm):
	class Meta:
		model = MobileService
		fields = [
			"provider",
			"phone",
			"servicetype",
			"monthlycost",
			"expiry",
		]
		widgets = {
            'expiry': DateInput(),
        }




class ElectricityServiceForm(forms.ModelForm):
	class Meta:
		model = ElectricityService
		fields = [
			"provider",
			"kwh",
		]
		widgets = {}


class BroadbandServiceForm(forms.ModelForm):
	class Meta:
		model = BroadbandService
		fields = [
			"provider",
			"GBpermonth",
			"monthlycost",
			"connectiontype",
			"expiry",
		]
		widgets = {
			'expiry': DateInput(),
		}






class SecurityServiceForm(forms.ModelForm):
	class Meta:
		model = SecurityService
		fields = [
			"interestedinsecuringhome",
			"provider",
			"monthlycost",
			"expiry",
		]
		widgets = {
			'expiry': DateInput(),
		}


class PhoneServiceForm(forms.ModelForm):
	class Meta:
		model = PhoneService
		fields = [
			"provider",
			"monthlycost",
			"expiry",
		]
		widgets = {
			'expiry': DateInput(),
		}


