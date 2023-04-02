from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name= 'home'),
    path('about/', views.About, name= 'about'),
    path('contact/', views.Contacts, name= 'contact'),
    path('blog/', views.Index_Blog, name= 'blog'),
    path('service/', views.Index_Service, name= 'service'),
    path('internshipdetails/', views.InternshipDetails, name= 'internshipdetails'),

]