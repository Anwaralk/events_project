from django.contrib import admin
from .models import Event

admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'event_date']
    list_display_links = ['event_name']
    list_filter = ['active']

# Register your models here.
