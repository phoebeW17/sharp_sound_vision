from django.contrib import admin
from .models import Portfolio
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Portfolio)

class PortfolioAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status',)
    search_fields = ('title', 'text')
    list_filter = ('status',)
    summernote_fields = ('content',)



