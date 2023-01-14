from django.contrib import admin
from .models import VideosDetails, Location, Item, UserDetails
# Register your models here.

admin.site.register(Location)
admin.site.register(Item)
admin.site.register(VideosDetails)
admin.site.register(UserDetails)