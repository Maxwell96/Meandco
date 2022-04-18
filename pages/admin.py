from django.contrib import admin
from .models import Page

# We have created a superuser and added some pages in the admin so:
# *We want to see when each page was last updated to keep track of changes to our site;
# *We want to display the page titles in alphabetical order to make them easier to browse; and
# *Once there are many pages, we want a handy way to search for a page.

#class PageAdmin(admin.ModelAdmin):
   # list_display = ('title', 'updated_date')
   # ordering = ('title',)
   # search_fields = ('title',)

# Register your models here.
admin.site.register(Page) #, PageAdmin

