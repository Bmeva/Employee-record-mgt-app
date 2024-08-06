from django.urls import path

from .import views

from .views import ProjectAPIviewset

# from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('MevabProject', ProjectAPIviewset, basename='MevabProject')


urlpatterns = router.urls

# urlpatterns = [
#     path('', views.home, name = 'home')
# ]