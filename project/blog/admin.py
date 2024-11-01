from django.contrib import admin
from .models import Blog
import admin_thumbnails

from django.urls import reverse
from django.utils.html import format_html

@admin_thumbnails.thumbnail('image')
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','is_active','image_thumbnail','edit_button', 'delete_button')
    prepopulated_fields = {'slug': ('title',)}
    
    actions = None
    def edit_button(self, obj):
        url = reverse('admin:blog_blog_change', args=[obj.pk])  
        return format_html('<a class="button" href="{}">Edit</a>', url)

    def delete_button(self, obj):
        url = reverse('admin:blog_blog_delete', args=[obj.pk])
        return format_html('<a class="button button-secondary" href="{}">Detele</a>', url)

    edit_button.short_description = 'Edit'
    delete_button.short_description = 'Delete'
    
admin.site.register(Blog,BlogAdmin)