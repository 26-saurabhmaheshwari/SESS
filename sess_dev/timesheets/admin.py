from django.contrib import admin

# Register your models here.
from .models import TimeRecords,TimeMenus

admin.site.register(TimeRecords)
admin.site.register(TimeMenus)