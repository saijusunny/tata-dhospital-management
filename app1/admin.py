from django.contrib import admin
from.models import section
from.models import staff
from.models import patient
from.models import doctor

# Register your models here.
admin.site.register(section)
class sectionadmin(admin.ModelAdmin):
    list_display = ('id', 'Section_name ', 'room_no')
admin.site.register(staff)
class staffadmin(admin.ModelAdmin):
    list_display = ('id', 'name ', 'username', 'password','number','section','mail', 'item')

admin.site.register(doctor)  
class doctoradmin(admin.ModelAdmin):
    list_display = ('id', 'name ', 'username', 'password','number','section','mail', 'item')

admin.site.register(patient)  
class patientadmin(admin.ModelAdmin):
    list_display = ('id', 'name ', 'address', 'mobile','email','age','section')