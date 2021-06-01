from django.contrib import admin
from django.utils.html import format_html
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('photo_main_tag', 'title_format', 'is_published', 'price', 'list_date', 'agent')
    list_display_links = ('title_format',)
    list_filter = ('agent',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 10

    def title_format(self, obj):
        return format_html('[{1}] {0}'.format(obj.title, obj.id))

    title_format.short_description = 'Headline'

    def photo_main_tag(self, obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.photo_main.url))

    photo_main_tag.short_description = 'Main Image'

admin.site.register(Listing, ListingAdmin)
