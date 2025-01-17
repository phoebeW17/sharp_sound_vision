from django.contrib import admin
from .models import Testimonial
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Testimonial)

class TestimonialAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'posted_on', 'status')
    search_fields = ('title', 'text')
    list_filter = ('status', 'posted_on')
    summernote_fields = ('content',)