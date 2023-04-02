from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def SignUp(request):
    if request.method=='POST':
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request,'Password is not matching. Please try with new Password')
            return redirect('/authentication/signup/')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email is taken")
                return redirect('/authentication/login/')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        myuser=authenticate(username=get_email, password=get_password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "User Created &Login Successfully.")
            return redirect('/')
        
        # messages.success(request, "User created successfully. Please login now!!")
        # return redirect('/authentication/login/')
    
    return render(request, 'authentication/signup.html')

def Login(request):
    if request.method == 'POST':
        get_email=request.POST.get('email')
        get_password=request.POST.get('password')
        myuser=authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'authentication/login.html')

def Logout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return render(request, 'authentication/login.html')