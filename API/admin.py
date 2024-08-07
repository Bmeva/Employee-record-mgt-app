

from django.contrib import admin

from .models import EmployeeDetails

from .models import *


#from authentication.models import User



class ProjectAdmin(admin.ModelAdmin):
    list_display =('first_name', 'id', 'last_name', 'start_date', 'status', 'created_at')
    list_editable = ('first_name', 'last_name')
    list_display_links = ('id', 'status')
    ordering= ('-id',)
    #readonly_fields = ('email', 'password',) to make fields uneditable
    #note you cannot add a many to many field in a list_display like the departments
   
    
  
    

admin.site.register(EmployeeDetails, ProjectAdmin)
admin.site.register(Training)
admin.site.register(EmployeeSkill)
admin.site.register(JobRequirement)
admin.site.register(TrainingNeed)




