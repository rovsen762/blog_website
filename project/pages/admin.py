from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone','email','created_at')
    actions = None
    
    
admin.site.register(Contact,ContactAdmin)