

from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout # visable pages using django login session method
from  django.contrib.auth.decorators import login_required
from app1.models import patient, staff, section
from app1.models import doctor

def index(request):
    return render(request, 'index.html')

#---------------------------------------------Signup Login Pages-----------------------------------------------
def signup(request):
    return render(request, 'signup.html')

def loginpage(request):
    return render(request, 'login.html')

@login_required(login_url='adminlogin')
def about(request):
    return render(request, 'about.html')

#**************************************************************************************************************



#--------------------------------------user create functions ----------------------------------------------------

#signup page
def usercreate(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']

        if password==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    password=password,
                    email=email,
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('signup')
        return redirect('adminlogin')
    else:
        return render(request, 'signup.html')

#login page
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # request.session['uid'] = user.id #visable pages using session method
        if user is not None:
            # login(request, user) #this function is login visable pages using django login session method
            auth.login(request, user)
            messages.info(request, f'Welcome {username}')#pass users name to welcome page
            return redirect('about')
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')



# logoutpage
@login_required(login_url='adminlogin') #login  session method
def adminlogout(request):
    auth.logout(request)
    return redirect('index')
#************************************************************************************************************************



#--------------------------------------------------------staff area------------------------------------------------------


# @login_required(login_url='adminlogin')
# def add_student(request):
#     if request.method== 'POST':
#         name=request.POST['name']
#         address=request.POST['addr']
#         dob=request.POST['age']
#         join=request.POST['date']
#         sel1=request.POST['sel']
#         course1= course.objects.get(id=sel1)
#         std=student(
#             std_name=name,
#             std_address=address,
#             std_age=dob,
#             join_date=join,
#             course=course1)
#         std.save()
#         return redirect('show')
#     return render(request, 'student.html')

def staff_login(request):
    return render(request, 'staff_login.html')

def staffreg(request):
    lt=section.objects.all()
    return render(request, 'staffreg.html',{'lt':lt})

def staff_signup(request):
    ct=section.objects.all()
    return render(request, 'staff_signup.html',{'ct':ct} )

def staff_home(request):
    return render(request, "staff_home.html")

def login_stf(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # request.session['uid'] = user.id #visable pages using session method
        if staff.objects.filter(username=username).exists():
            if staff.objects.filter(password=password).exists():
                return redirect('staff_home')
            else:
                messages.info(request, 'invalid username and password, try again')
                return redirect('loginpage')

        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

def login_staff(request):
    if request.method=="POST":
        nm=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']
        sec=request.POST['sct']
        course1= section.objects.get(id=sec)
        nb=request.POST['phnumber']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image = "static/image/default.jpg"
        if password==cpass:
            if staff.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=staff(
                    name=nm,
                    username=username,
                    password=password,
                    mail=email,
                    section=course1,
                    number=nb,
                    item=image,
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('staffreg')
        return redirect('staff_login')
    else:
        return render(request, 'staffreg.html')
   

#-----------------------------------------------------login doctor--------------------------------
def doctor_login(request):
    return render(request, 'doctor_login.html')

#doctor signup page
def log(request):
    ct=section.objects.all()
    return render(request, 'doctorreg.html',{'ct':ct} )



# def doctor_signup(request):
#     return render(request, "doctor_signup.html")

def doctor_home(request):
    return render(request, "doctor_home.html")

def doctor_stf(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # request.session['uid'] = user.id #visable pages using session method
        if doctor.objects.filter(username=username).exists():
            if doctor.objects.filter(password=password).exists():
                return redirect('doctor_home')
            else:
                messages.info(request, 'invalid username and password, try again')
                return redirect('loginpage')

        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

def login_doctor(request):
    if request.method=="POST":
        nm=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']
        sec=request.POST['sct']
        course1= section.objects.get(id=sec)
        nb=request.POST['phnumber']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image = "static/image/default.jpg"
        if password==cpass:
            if doctor.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=doctor(
                    name=nm,
                    username=username,
                    password=password,
                    mail=email,
                    section=course1,
                    number=nb,
                    items=image,
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('log')
        return redirect('doctor_login')
    else:
        return render(request, 'doctorreg.html')
   

#***************************************************************

#--------------------------------------------patient registration--------------------------------------------
def  patient_reg_page(request):
    pt=section.objects.all()
    return render(request, 'patient_reg.html',{'pt':pt})
    
def patient_reg(request):
    if request.method== 'POST':
            name=request.POST['name']
            address=request.POST['address']
            mob=request.POST['mobile']
            em=request.POST['email']
            dob=request.POST['age']
            sec=request.POST['sct']
            course1= section.objects.get(id=sec)
            std=patient(
                name=name,
                address=address,
                mobile=mob,
                email=em,
                age=dob,
                section=course1,
                )
            std.save()
            return redirect('staff_home')
    return render(request, 'patient_reg.html')



#patient View in doctor section

def patient_view_doctor(request):
        result= patient.objects.all()
        return render(request, 'patient_view_doctor.html',{'result':result})
# add student functions
# @login_required(login_url='adminlogin')
# def add_student(request):
#     if request.method== 'POST':
#         name=request.POST['name']
#         address=request.POST['addr']
#         dob=request.POST['age']
#         join=request.POST['date']
#         sel1=request.POST['sel']
#         course1= course.objects.get(id=sel1)
#         std=student(
#             std_name=name,
#             std_address=address,
#             std_age=dob,
#             join_date=join,
#             course=course1)
#         std.save()
#         return redirect('show')
#     return render(request, 'student.html')


#**************************************section*********************************************
def sections(request):  #corses
    return render(request,'section.html')

def course1(request):
    uid=User.objects.get(id=request.session['uid'])
    return render(request, 'section.html', {'uid':uid})
    

def add_section(request):
    if request.method== 'POST':
        cors=request.POST['section']
        cfee=request.POST['floor']
        crs=section()
        crs.Section_name=cors
        crs.room_no=cfee
        crs.save()
        return redirect('about')
    return redirect("section.html")



def doctor_signup(request):
    courses=section.objects.all()
    return render(request,'doctor_signup.html', {'courses':courses})