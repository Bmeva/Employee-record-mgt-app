from rest_framework import serializers
from .models import EmployeeDetails

class EmployeeDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        #fields = ('project_name', 'project_owner', 'start_date', 'end_date', 'comments', 'status')
        exclude = ('created_at', 'modified_at')
        #if you want to include all fields just stop at model = EmployeeDetails