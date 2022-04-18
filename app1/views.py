

import os
from pydoc import doc
from queue import Empty
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

def logs_all(request):
    return render(request, 'login._all.html')


# login all
def login_all(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # request.session['uid'] = user.id #visable pages using session method
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                # login(request, user) #this function is login visable pages using django login session method
                auth.login(request, user)
                messages.info(request, f'Welcome {username}')#pass users name to welcome page
                return redirect('about')
            else:
                messages.info(request, 'invalid username and password, try again')
                return redirect('logs_all')

        elif staff.objects.filter(username=username).exists():
           
            if staff.objects.filter(password=password).exists():
                    ps=staff.objects.filter(username=username )
                    return render(request,'staff pro.html',{'ps':ps})

            else:
                messages.info(request, 'invalid username and password, try again')
                return redirect('logs_all')
        elif doctor.objects.filter(username=username).exists():
            if doctor.objects.filter(password=password).exists():
                pkl=doctor.objects.filter(username=username )
                return render(request,'doctor pro.html',{'ps':pkl})
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('logs_all')
    else:
        return redirect('logs_all')

#sign up all pages
def sign_all(request):
    ltts=section.objects.all()
    return render(request,'signup_all.html', {'ltts':ltts})

# Signup all function
def signup_all(request):
    if request.method=="POST":
        usr=request.POST['username']
        if User.objects.filter(username=usr).exists():
            messages.info(request, 'Username Is Already Exist,Please Add diffrent Username, And Try Again')
            return redirect('sign_all')
        elif staff.objects.filter(username=usr).exists():
            messages.info(request, 'Username Is Already Exist,Please Add difffrent Username, And Try Again')
            return redirect('sign_all')
        elif doctor.objects.filter(username=usr).exists():
            messages.info(request, 'Username Is Already Exist,Please Add difffrent Username, And Try Again')
            return redirect('sign_all')
        else:
            destination = request.POST['destini']
            if destination=="STAFF":
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
            elif destination=="DOCTOR":
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
                return redirect ('sign_all')

        
    else:
        return render(request, 'signup.html')

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

#staff Home
def staff_home(request):
    return render(request, "staff_home.html")


#login Staff 
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
    lkt=patient.objects.all()
    stc=section.objects.all()
    return render(request,'patient_view_doctor.html',{'stc':stc, 'lkt':lkt})


def patient_flt(request):
    sect=request.POST['sct']
    if sect=='All Sections':
        return redirect('patient_view_doctor')
    else:
        print(sect)
        stc=section.objects.all()
        lkt=patient.objects.filter(section=sect)
        return render(request,'patient_view_doctor.html',{'lkt':lkt,'stc':stc, 'sect':sect})



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
    
#Add Section

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
#admin Doctor profile view
@login_required(login_url='adminlogin')
def admin_doct_view(request):
    stc=section.objects.all()
    dt=doctor.objects.all()
    return render(request, 'admin_doct_views.html', {'dt':dt, 'stc':stc})
#admin doctor View filter
@login_required(login_url='adminlogin')
def admin_doct_flt(request):
    sect=request.POST['sct']
    if sect=='All Sections':
        return redirect('admin_doct_view')
    else:
        print(sect)
        stc=section.objects.all()
        dt=doctor.objects.filter(section=sect)
        return render(request,'admin_doct_views.html',{'dt':dt,'stc':stc})

#admin  staff filter view

@login_required(login_url='adminlogin')

def admin_staff_flt(request):
    sect=request.POST['sct']
    if sect=='All Sections':
        return redirect('admin_staff_view')
    else:
        print(sect)
        stc=section.objects.all()
        dt=staff.objects.filter(section=sect)
        return render(request,'admin_stf_view.html',{'dt':dt,'stc':stc})

#admin staff view
@login_required(login_url='adminlogin')
def admin_staff_view(request):
    stc=section.objects.all()
    dt=staff.objects.all()
    return render(request, 'admin_stf_view.html', {'dt':dt, 'stc':stc})

#admin patient view
@login_required(login_url='adminlogin')
def admin_patient_view(request):
    lkt=patient.objects.all()
    stc=section.objects.all()
    return render(request,'admin_patient details.html',{'stc':stc, 'lkt':lkt})

#admin patient filter
@login_required(login_url='adminlogin')
def admin_patient_flt(request):
    sect=request.POST['sct']
    if sect=='All Sections':
        return redirect('admin_patient_view')
    else:
        print(sect)
        stc=section.objects.all()
        lkt=patient.objects.filter(section=sect)
        return render(request,'admin_patient details.html',{'lkt':lkt,'stc':stc, 'sect':sect})



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

# admin complete profile 
@login_required(login_url='adminlogin')
def complete_pro(request):
    return render(request,'admin_signup_pro.html')

#admin Profile View
@login_required(login_url='adminlogin')
def profile_admin(request):
    result=userlogin.objects.filter(user=request.user.id).last()
    return render(request,'profile_admin.html', {'result':result})

#admin edit profile page
@login_required(login_url='adminlogin')
def edit_admin_pro(request,pk):
    products=userlogin.objects.get(id=pk)
    return render(request,'admin_edit.html', {'products':products})


#admin edit function
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


#admin patient approve page

@login_required(login_url='adminlogin')
def admin_aprove(request,pk):
    ltt=patient.objects.get(id=pk)
    return render(request, 'admin_patient_aprovel.html',{'ltt':ltt})

    #admin send aprove through email
@login_required(login_url='adminlogin')     
def admin_send_aprove(request):
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
            subject='Visiting Message From Ap Varkey Mission Hospital  ' #subject
            message='Dear, '+name+'\n\n Your Checkup Request is Accepted \n\nConselted By: Dr.'+dct+ '\n\n\nVisiting Time:'+tiaf+'To'+tibf+'\n\nVisiting Date:'+dt+'\n\n\n Help Desk No:0000124578 \n\n\n Help Desk Email:saijusunny1301@gmail.com\n\n\n Please Visit Before The Given Ending Time \n\n\n Thank You' #messege
            recipient=em
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            return redirect('admin_patient_view')
     return render(request, 'admin_patient_aprovel.html')

#admin delete patient
def admin_delete_patient(request,pk):
    products=patient.objects.get(id=pk)
    products.delete()
    return redirect('admin_patient_view')

#send mail
from django.conf import settings

from django.core.mail import send_mail

#doctor patient aprove page

def aprove(request,pk):
    ltt=patient.objects.get(id=pk)
    return render(request, 'patient_aprovel.html',{'ltt':ltt})
      

#doctor patient aprove
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
            subject='Visiting Message From Ap Varkey Mission Hospital  ' #subject
            message='Dear, '+name+'\n\n Your Checkup Request is Accepted \n\nConselted By: Dr.'+dct+ '\n\n\nVisiting Time:'+tiaf+'To'+tibf+'\n\nVisiting Date:'+dt+'\n\n\n Help Desk No:0000124578 \n\n\n Help Desk Email:saijusunny1301@gmail.com\n\n\n Please Visit Before The Given Ending Time \n\n\n Thank You' #messege
            recipient=em
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            return redirect('patient_view_doctor')
     return render(request, 'patient_aprovel.html')

#admin delete staff
@login_required(login_url='adminlogin')
def admin_delete_staff(request,pk):
    products=staff.objects.get(id=pk)
    if not products.item =="static/image/icon.png":
        os.remove(products.item.path)
    else:
        pass
    products.delete()
    products.delete()
    return redirect('admin_staff_view')


#admin delete doctor
@login_required(login_url='adminlogin')
def admin_delete_doctor(request,pk):
    products=doctor.objects.get(id=pk)
    if not products.items =="static/image/icon.png":
        os.remove(products.items.path)
    else:
        pass
    products.delete()
    return redirect('admin_doct_view')

#delete patient
@login_required(login_url='adminlogin')
def delete_patient(request,pk):
    products=patient.objects.get(id=pk)
    products.delete()
    return redirect('patient_view_doctor')

#delete admin profile
@login_required(login_url='adminlogin')
def delete_admin(request,pk):
    products=userlogin.objects.get(id=pk)
    if not products.image =="static/image/icon.png":
                os.remove(products.image.path)
    else:
        pass
    products.delete()
    return redirect('adminlogin')

#Edit doctors:

def edit_doctor(request,pk):
    products=doctor.objects.get(id=pk)
    sec=section.objects.all()
    return render(request,'edit_doctors pro.html', {'products':products, 'sec':sec})

@login_required(login_url='adminlogin')
def edit_doctor_details(request,pk):
    if request.method=='POST':
        products = doctor.objects.get(id=pk)
        products.name=request.POST.get('name')
        products.username=request.POST.get('username')
        products.password=request.POST.get('password')
        products.number=request.POST.get('number')
        products.mail=request.POST.get('mail')
      
        sec=request.POST['sct']
        course1= section.objects.get(id=sec)
        products.section=course1
        products.save()
        return redirect('admin_doct_view')
    return render(request, 'admin_doct_views.html')

#edit staff
def edit_staff(request,pk):
    products=staff.objects.get(id=pk)
    sec=section.objects.all()
    return render(request,'edit_taff_pro.html', {'products':products, 'sec':sec})

@login_required(login_url='adminlogin')
def edit_staff_details(request,pk):
    if request.method=='POST':
        products = staff.objects.get(id=pk)
        products.name=request.POST.get('name')
        products.username=request.POST.get('username')
        products.password=request.POST.get('password')
        products.number=request.POST.get('number')
        products.mail=request.POST.get('mail')
      
        sec=request.POST['sct']
        course1= section.objects.get(id=sec)
        products.section=course1
        products.save()
        return redirect('admin_staff_view')
    return render(request, 'admin_stf_view.html')
