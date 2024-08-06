from rest_framework import serializers
from .models import WorkProject

class WorkProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkProject
        fields = ('project_name', 'project_owner', 'start_date', 'end_date', 'comments', 'status')
        #exclude = ('created_at', 'modified_at')
        #if you want to include all fields just stop at model = WorkProject