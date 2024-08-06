

from django.contrib import admin

from .models import WorkProject


#from authentication.models import User



class ProjectAdmin(admin.ModelAdmin):
    list_display =('project_name', 'id', 'project_owner', 'start_date', 'end_date', 'status', 'created_at', 'modified_at')
    list_editable = ('project_name', 'project_owner')
    list_display_links = ('id', 'status')
    ordering= ('-id',)
    #readonly_fields = ('email', 'password',) to make fields uneditable
   
    
  
    

admin.site.register(WorkProject, ProjectAdmin)


