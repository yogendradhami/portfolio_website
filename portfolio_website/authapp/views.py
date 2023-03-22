from django.shortcuts import render

# Create your views here.
def SignUp(request):
    return render(request, 'authentication/signup.html')

def Login(request):
    return render(request, 'authentication/login.html')

def Logout(request):
    return render(request, 'authentication/login.html')