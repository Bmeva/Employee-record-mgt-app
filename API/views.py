from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeeDetails

from rest_framework import viewsets, permissions

from .serializers import EmployeeDetailsSerializers  
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

def home(request):
    
    return HttpResponse('Welcome to our home page')

class EmpAPIviewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    #permission_classes = [IsAuthenticated]
    
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializers
    
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
        mevabemp= self.queeryset.get(pk=pk)
        serializer = self.serializer_class(mevabemp)
        return Response(serializer.data)

    def update(self, request, pk=None):
        mevabemp = self.queeryset.get(pk=pk)
        serializer = self.serializer_class(mevabemp, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        mevabemp = self.queeryset.get(pk=pk)
        mevabemp.delete()
        return Response(status=204)
        
    
