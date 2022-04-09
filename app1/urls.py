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
    path('staff_logs', views.staff_logs, name="staff_logs"),
    

    
#*********************************************************************************************



#-----------------------Doctor Login Area ----------------------------------------------------------------

    path('doctor_login', views.doctor_login, name="doctor_login"),
    path('doctor_signup', views.doctor_signup, name="doctor_signup"),
    path('login_doctor', views.login_doctor, name="login_doctor"),
    path('doctor_home', views.doctor_home, name="doctor_home"),
    path('doctor_stf', views.doctor_stf, name="doctor_stf"),
    path('pro_doctor',views.pro_doctor,name='pro_doctor'),
    path('doctor_logs', views.doctor_logs, name="doctor_logs"),
    
#**********************************************************************************************************
    


#--------------------------------------patient-----------------------------------------------------------------
path('patient_reg_page', views.patient_reg_page, name='patient_reg_page'),
path('patient_reg', views.patient_reg, name='patient_reg'),
path('patient_view_doctor', views.patient_view_doctor, name='patient_view_doctor'),
path('delete_patient/<int:pk>', views.delete_patient, name='delete_patient'),
#*************************************************************************************************************



#-------------------------------------------------user create function ---------------------------------------
    path('usercreate/', views.usercreate, name='usercreate'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
#-------------------------------------------------------------------------------------------------------------
    


#---------------------------------section----------------------------
path('section_view',views.section_view, name='section_view'),
path('add_section',views.add_section, name='add_section'),
path('course1',views.course1, name='course1'),
path('log',views.log, name='log'),
path('staffreg',views.staffreg, name='staffreg'),
path('edit_section/<int:pk>',views.edit_section, name='edit_section'),
path('section_edit/<int:pk>',views.section_edit, name='section_edit'),
path('delete_section/<int:pk>',views.delete_section, name='delete_section'),



#------------------------------adminb Views----------------
path('admin_doct_view', views.admin_doct_view, name='admin_doct_view'),
path('admin_staff_view', views.admin_staff_view, name='admin_staff_view'),
path('admin_patient_view', views.admin_patient_view, name='admin_patient_view'),
path('signup_details', views.signup_details, name='signup_details'),
path('complete_pro', views.complete_pro, name='complete_pro'),
path('profile_admin', views.profile_admin, name='profile_admin'),
path('edit_details/<int:pk>', views.edit_details, name='edit_details'),
path('edit_admin_pro/<int:pk>', views.edit_admin_pro, name='edit_admin_pro'),
path('aprove/<int:pk>',views.aprove, name='aprove'),
path('send_aprove',views.send_aprove, name='send_aprove'),

]