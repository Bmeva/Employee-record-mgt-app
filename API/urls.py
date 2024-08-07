from django.urls import path

from .import views

from .views import EmpAPIviewset

# from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Mevaemprec', EmpAPIviewset, basename='Mevaemprec')


urlpatterns = router.urls

# urlpatterns = [
#     path('', views.home, name = 'home')
# ]