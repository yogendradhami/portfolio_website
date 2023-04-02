from django.shortcuts import render,redirect
from  django.contrib import messages
from portfolio.models import Contact,Blog,Internship
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

    # for user authentication to check whether the particular user already registeres or not

    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page.")
        return redirect("/authentication/login/")
    
# this is  the post request for form
    if request.method == 'POST':
        fname =request.POST.get('full_name')
        fusn=request.POST.get('usn')
        femail=request.POST.get('email')
        
        fcollege=request.POST.get('cname')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')

# converting into  upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprojreport=fprojreport.upper()
        foffer=foffer.upper()

        # check conditions
        check1= Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request, "Your Details are Stored Already.")
            return redirect('/internshipdetails')

        query=Internship(full_name=fname,email=femail, usn=fusn,college_name=fcollege, offer_status=foffer, start_date=fstartdate, end_date=fenddate, project_report=fprojreport)
        query.save()


        messages.success(request, "Form is submitted successfully.")
        return redirect('/internshipdetails')

    return render(request, 'internship.html')