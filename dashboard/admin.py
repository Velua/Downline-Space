from django.contrib import admin

# Register your models here.


from .models import Quote, FacebookFriendUpload

admin.site.register(Quote)
admin.site.register(FacebookFriendUpload)