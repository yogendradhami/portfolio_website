from django.shortcuts import render,redirect
from  django.contrib import messages
from portfolio.models import Contact,Blog
# Create your views here.
def Home(request):
    return render(request, 'layouts/master.html')

def About(request):
    return render(request, 'about.html')

def Contacts(request):
    if request.method == 'POST':
        con=Contact()
        con.name=request.POST.get('name')
        con.email=request.POST.get('email')
        con.number = request.POST.get('number')
        con.description= request.POST.get('description')
        con.save()
        messages.success(request, "Thanks for contacting. We will get by you soon")
        return redirect('contact')


    return render(request, 'contact.html')

def Index_Blog(request):
    posts= Blog.objects.all()
    context={"posts":posts}
    return render(request, 'blog.html',context)

def Index_Service(request):
    return render(request, 'service.html')

def InternshipDetails(request):
    return render(request, 'internship.html')