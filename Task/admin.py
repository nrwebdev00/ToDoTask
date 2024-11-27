from django.contrib import admin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish_date','priority','visibility']
    list_filter = ['title','details','priority','visibility']
    search_fields = ['title','priority','visibility']
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish_date'
    ordering = ['priority','publish_date']
    show_facets = admin.ShowFacets.ALWAYS