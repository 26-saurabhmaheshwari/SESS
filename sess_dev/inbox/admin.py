from django.contrib import admin

# Register your models here.
from .models import InboxHeader , InboxBody , InboxRecipient

admin.site.register(InboxHeader)
admin.site.register(InboxBody)
admin.site.register(InboxRecipient)