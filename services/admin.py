from django.contrib import admin
from .models import Service
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status')
    search_fields = ('title', 'description')
    list_filter = ('status',)
    summernote_fields = ('description',)
