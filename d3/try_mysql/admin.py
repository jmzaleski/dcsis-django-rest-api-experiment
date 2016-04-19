from django.contrib import admin

from django.contrib import admin
from try_mysql.models import Person
     
class PersonAdmin(admin.ModelAdmin):
        # fields display on change list
        list_display = ['first_name', 'last_name', 'email']
        # fields to filter the change list with
        list_filter = ['last_name', 'email']
        # fields to search in change list
        search_fields = ['first_name', 'last_name', 'email']
        # enable the date drill down on change list
        #date_hierarchy = 'created'
        # enable the save buttons on top on change form
        save_on_top = True
        # prepopulate the slug from the title - big timesaver!
        #prepopulated_fields = {"slug": ("title",)}
     
admin.site.register(Person, PersonAdmin)# Register your models here.
