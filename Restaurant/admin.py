from django.contrib import admin
from .models import  Restaurant
# Register your models here.

class ResturantAdmin(admin.ModelAdmin):
    list_display=('user','restaurant_name','is_approved','created_at',)
    list_display_links=('user','restaurant_name')

admin.site.register(Restaurant,ResturantAdmin)

