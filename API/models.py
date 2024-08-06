from django.db import models

# Create your models here.


class WorkProject(models.Model):
    project_name = models.CharField(unique=True, max_length=120)
    project_owner = models.CharField(unique=True, max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(blank=True, null=True, max_length=600)
    status = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Project_name}  {self.id}"