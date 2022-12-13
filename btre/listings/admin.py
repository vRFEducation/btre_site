from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','list_date')
    list_editable = ('is_published', 'price')
    search_fields = ('title', 'city', 'state')
    list_per_page = 4


admin.site.register(Listing, ListingAdmin)

