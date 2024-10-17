# Description: This file contains the URL patterns for the core app. The router is used to register the viewsets and create the URLs for the API endpoints. The include function is used to include the URLs from the router in the main URL configuration of the project.

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet,
    EmployerViewSet,
    JobListingViewSet,
    JobApplicationViewSet,
    HiringViewSet
)

# Create a router and register viewsets
router = DefaultRouter()

router.register(r'employees', EmployeeViewSet)
router.register(r'employers', EmployerViewSet)
router.register(r'jobs', JobListingViewSet)
router.register(r'applications', JobApplicationViewSet)
router.register(r'hirings', HiringViewSet)

# Use the router's URLs
urlpatterns = [
    path('', include(router.urls)),
]