

import os
from pydoc import doc
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout # visable pages using django login session method
from  django.contrib.auth.decorators import login_required
from app1.models import patient, staff, section
from app1.models import doctor
from .models import userlogin

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

def staff_logs(request):
    return render(request, 'staff_login_pro.html')

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
                ps=staff.objects.filter(username=username )
                return render(request,'staff pro.html',{'ps':ps})

            else:
                messages.info(request, 'invalid username and password, try again')
                return redirect('staff_login')

        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('staff_login')
    else:
        return redirect('staff_login')

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
            image = "static/image/icon.png"
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


def doctor_logs(request):
    return render(request, 'doctor_login_pro.html')

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
                ps=doctor.objects.filter(username=username )
                return render(request,'doctor pro.html',{'ps':ps})
            else:
                messages.info(request, 'invalid username and password, try again')
                return redirect('doctor_login')

        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('doctor_login')
    else:
        return redirect('doctor_login')

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
            image = "static/image/icon.png"
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
   

# def edit_details(request,pk):
#     empl=images.objects.get(id=pk)
#     form=image_form(instance=empl)
#     if request.method =='POST':
#         form=image_form(request.POST,instance=empl)
#         if form.is_valid():
#             form.save()
#             return redirect('view')
#     return render(request,'edit.html',{'form':form})
   #doctor view
def pro_doctor(request):

    pass

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
    print ("hai")
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

def delete_section(request,pk):
    products=section.objects.get(id=pk)
    products.delete()
    return redirect('section_view')

#edit section
def section_edit(request,pk):
    sect=section.objects.get(id=pk)
    return render(request,'section._edit.html',{'sect':sect})

def edit_section(request,pk):
        if request.method=='POST':
            products = section.objects.get(id=pk)
            products.Section_name=request.POST.get('section_name')
            products.room_no=request.POST.get('room_no')
            products.save()
            return redirect('section_view')
        return render(request, 'section.html')
    

def section_view(request):
    sec=section.objects.all()
    return render(request,'section.html',{'sec':sec})

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
        return redirect('section_view')
    return redirect("section.html")



def doctor_signup(request):
    courses=section.objects.all()
    return render(request,'doctor_signup.html', {'courses':courses})



#----admin view-------------------------------------
def admin_doct_view(request):
    dt=doctor.objects.all()
    return render(request, 'admin_doct_views.html', {'dt':dt})

def admin_staff_view(request):
    dt=staff.objects.all()
    return render(request, 'admin_stf_view.html', {'dt':dt})

def admin_patient_view(request):
    dt=patient.objects.all()
    return render(request, 'admin_patient details.html', {'dt':dt})


#admin signup
#compltet profile section
@login_required(login_url='adminlogin')
def signup_details(request):
    if request.method == "POST":
        nm=request.POST['name']
        uname=request.POST['username']
        upass=request.POST['password']
        repas=request.POST['repassword']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image = "static/image/icon.png"
        eum=request.POST['email']
        uid= User.objects.get(id=request.user.id)
        print(uid)

        result=userlogin(
            name=nm,
            username=uname,
            password=upass,
            repassword=repas,
            image=image,
            email=eum,
            user=uid,
                            
            )
        result.save()
        return redirect('profile_admin')


@login_required(login_url='adminlogin')
def complete_pro(request):
    return render(request,'admin_signup_pro.html')

@login_required(login_url='adminlogin')
def profile_admin(request):
    result=userlogin.objects.filter(user=request.user.id).last()
    return render(request,'profile_admin.html', {'result':result})

@login_required(login_url='adminlogin')
def edit_admin_pro(request,pk):
    products=userlogin.objects.get(id=pk)
    return render(request,'admin_edit.html', {'products':products})

@login_required(login_url='adminlogin')
def edit_details(request,pk):
    if request.method=='POST':
        products = userlogin.objects.get(id=pk)
        products.name=request.POST.get('name')
        products.username=request.POST.get('username')
        products.password=request.POST.get('password')
        products.repassword=request.POST.get('repassword')
        products.email=request.POST.get('email')
        # if len(products.image)>0:
        #     os.remove(products.image.path)
        if request.FILES.get('file') is not None:
            print('hai')
            if not products.image =="static/image/icon.png":
                os.remove(products.image.path)
                products.image = request.FILES['file']
            else:
                products.image = request.FILES['file']
        else:
            os.remove(products.image.path)
            products.image ="static/image/icon.png"
        
        products.save()
        return redirect('profile_admin')
    return render(request, 'admin_edit.html')


#send mail
from django.conf import settings

from django.core.mail import send_mail


def aprove(request,pk):
    ltt=patient.objects.get(id=pk)
    return render(request, 'patient_aprovel.html',{'ltt':ltt})
      
def send_aprove(request):
     if request.method=='POST':
            name=request.POST['name']
            address=request.POST['address']
            mob=request.POST['mobile']
            em=request.POST['email']
            dob=request.POST['age']
            sec=request.POST['sct']
            tibf=request.POST['timebf']
            tiaf=request.POST['timeaf']
            dt=request.POST['date']
            dct=request.POST['dctr']
            print(name)
            print(address)
            print(mob)
            print(dob)
            print(sec)
            print(tiaf)
            print(dt) 
            subject='Lerning softwere' #subject
            message='Dear, '+name+'\n\n Your Checkup Request is Accepted \n\nConselted By: Dr.'+dct+ '\n\n\nVisiting Time:'+tiaf+'To'+tibf+'\n\nVisiting Date:'+dt+'\n\n\n Help Desk No:0000124578 \n\n\n Help Desk Email:saijusunny1301@gmail.com\n\n\n Please Visit Before The Given Ending Time \n\n\n Thank You' #messege
            recipient=em
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            return redirect('patient_view_doctor')
     return render(request, 'patient_aprovel.html')


def delete_patient(request,pk):
    products=patient.objects.get(id=pk)
    products.delete()
    return redirect('patient_view_doctor')
