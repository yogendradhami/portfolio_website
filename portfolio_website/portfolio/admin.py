from django.contrib import admin
from.models import Contact,Blog, Internship
# Register your models here.

admin.site.register(Contact)
admin.site.register(Blog)


class InternshipAdmin(admin.ModelAdmin):
    list_display = ('full_name',
    'usn',
    'email',
    'college_name',
    'offer_status',
    'start_date',
    'end_date',
    'project_report')

admin.site.register(Internship,InternshipAdmin)
# to rename the admin panel records

admin.site.site_header= "Portfolio"
admin.site.site_title= 'Portfolio'
admin.site.index_title= 'Admin_panel'