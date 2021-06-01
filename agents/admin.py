from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'name', 'email', 'phone', 'hire_date', 'is_mvp')
    list_display_links = ('name', 'email')
    list_filter = ('name',)
    list_editable = ('is_mvp',)
    search_fields = ('name', 'email', 'phone')
    list_per_page = 10

admin.site.register(Agent, AgentAdmin)
