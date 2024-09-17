from django.contrib import admin
from . models import Meetup, Location
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['date', 'location']
    prepopulated_fields = {'slug':('title',)}
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['suburb', 'city', 'province', 'country']

admin.site.register(Location, LocationAdmin)
admin.site.register(Meetup, MeetupAdmin)

