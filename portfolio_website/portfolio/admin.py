from django.contrib import admin
from.models import Contact
# Register your models here.

admin.site.register(Contact)

# to rename the admin panel records

admin.site.site_header= "Portfolio"
admin.site.site_title= 'Portfolio'
admin.site.index_title= 'Admin_panel'