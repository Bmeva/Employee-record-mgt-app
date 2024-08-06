from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkProject

from rest_framework import viewsets, permissions

from .serializers import WorkProjectSerializers
from rest_framework.response import Response

# Create your views here.

def home(request):
    
    return HttpResponse('Welcome to our home page')

class ProjectAPIviewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = WorkProject.objects.all()
    serializer_class = WorkProjectSerializers
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) #to display many records
        return Response(serializer.data)
        #At this point point you can check the url and you would see all records
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        mevabproject = self.queeryset.get(pk=pk)
        serializer = self.serializer_class(mevabproject)
        return Response(serializer.data)

    def update(self, request, pk=None):
        mevabproject = self.queeryset.get(pk=pk)
        serializer = self.serializer_class(mevabproject, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        mevabproject = self.queeryset.get(pk=pk)
        mevabproject.delete()
        return Response(status=204)
        
    
