from django.contrib import admin

# Register your models here.
from .models import Member, Person, Activity, FriendCSVUpload



admin.site.register(Person)

admin.site.register(Member)
admin.site.register(Activity)
admin.site.register(FriendCSVUpload)