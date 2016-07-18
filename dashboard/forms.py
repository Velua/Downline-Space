from django import forms


from .models import FacebookFriendUpload

# class CSVForm(forms.ModelForm):
# 	class Meta:
# 		model = CSVUpload
# 		fields = [
# 			"csvfile",
# 		]

class FacebookFriendsForm(forms.ModelForm):
	class Meta:
		model = FacebookFriendUpload
		fields = [
			"friendsfile",
		]