from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']
    list_display_links = ['name', 'date']

# class EventAdmin(admin.ModelAdmin):
#     list_display = ['id', 'event_name', 'event_date']
#     list_display_links = ['event_name']
#     list_filter = ['active']

#     fieldsets = (

#         ('Localizations', ('fields': [event_name, []]))

#     )

# Register your models here.
