from django.shortcuts import render,redirect
from  django.contrib import messages
from portfolio.models import Contact
# Create your views here.
def Home(request):
    return render(request, 'layouts/master.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    if request.method== 'POST':
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fnumber=request.POST.get('number')
        fdescription=request.POST.get('description')
        query=Contact(name=fname,email=femail,number=fnumber,description=fdescription)
        query.save()
        messages.success(request, "Thanks for contacting. We will get by you soon")
        
        return redirect('/contact')

    return render(request, 'contact.html')