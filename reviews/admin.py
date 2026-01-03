from django.contrib import admin
from .models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie_title','rating','user','created_at')
    search_fields = ('movie_title',"review_content")
    list_filter = ('rating','created_at')