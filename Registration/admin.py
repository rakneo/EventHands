from django.contrib import admin
from .models import RegisterDesk, EventList, SiteConfig
# Register your models here.

admin.site.register(RegisterDesk)
admin.site.register(EventList)
admin.site.register(SiteConfig)
