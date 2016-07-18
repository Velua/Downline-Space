from django.contrib import admin

# Register your models here.
from .models import MobileService, BroadbandService, ElectricityService, PhoneService, SecurityService

admin.site.register(MobileService)
admin.site.register(BroadbandService)
admin.site.register(ElectricityService)
admin.site.register(PhoneService)
admin.site.register(SecurityService)