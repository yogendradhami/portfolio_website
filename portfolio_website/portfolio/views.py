from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'layouts/master.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')