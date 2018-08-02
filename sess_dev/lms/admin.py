from django.contrib import admin

# Register your models here.
from .models import lms_count,lms_details

admin.site.register(lms_count)
admin.site.register(lms_details)