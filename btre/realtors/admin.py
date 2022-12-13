from django.contrib import admin
from realtors.models import Realtor

from django.utils.html import format_html

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px;max-height:100px;" /> '.format(obj.photo.url))
        

# admin.site.register(Realtor)