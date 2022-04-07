from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
   

#------------------------------------------------home area -------------------------------------
    path('', views.index, name='index'),
#************************************************************************************************




#-------------------------------------admin Signup Area----------------------------------------
    path('signup/', views.signup, name='signup'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('about/', views.about, name='about'),
#**************************************************************************************




#------------------------staff login area ------------------------------------------
    path('staff_login', views.staff_login, name="staff_login"),
    path('staff_signup', views.staff_signup, name="staff_signup"),
    path('login_staff', views.login_staff, name="login_staff"),
    path('staff_home', views.staff_home, name="staff_home"),
    path('login_stf', views.login_stf, name="login_stf"),
    
#*********************************************************************************************



#-----------------------Doctor Login Area ----------------------------------------------------------------

    path('doctor_login', views.doctor_login, name="doctor_login"),
    path('doctor_signup', views.doctor_signup, name="doctor_signup"),
    path('login_doctor', views.login_doctor, name="login_doctor"),
    path('doctor_home', views.doctor_home, name="doctor_home"),
    path('doctor_stf', views.doctor_stf, name="doctor_stf"),
#**********************************************************************************************************
    


#--------------------------------------patient-----------------------------------------------------------------
path('patient_reg_page', views.patient_reg_page, name='patient_reg_page'),
path('patient_reg', views.patient_reg, name='patient_reg'),
path('patient_view_doctor', views.patient_view_doctor, name='patient_view_doctor'),
#*************************************************************************************************************



#-------------------------------------------------user create function ---------------------------------------
    path('usercreate/', views.usercreate, name='usercreate'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
#-------------------------------------------------------------------------------------------------------------
    


#---------------------------------section----------------------------
path('sections',views.sections, name='sections'),
path('add_section',views.add_section, name='add_section'),
path('course1',views.course1, name='course1'),
path('log',views.log, name='log'),
path('staffreg',views.staffreg, name='staffreg'),
]