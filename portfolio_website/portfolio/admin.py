from django.contrib import admin
from.models import Contact,Blog
# Register your models here.

admin.site.register(Contact)
admin.site.register(Blog)

# to rename the admin panel records

admin.site.site_header= "Portfolio"
admin.site.site_title= 'Portfolio'
admin.site.index_title= 'Admin_panel'