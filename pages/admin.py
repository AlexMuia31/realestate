from django.contrib import admin
from .models import home
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header ='Real Estate' #changes the header of the admin page
admin.site.unregister(Group) #removes group from admin


class homeAdmin(admin.ModelAdmin):  #what to display in admin
    list_display = ("name", "address")

admin.site.register(home, homeAdmin)
