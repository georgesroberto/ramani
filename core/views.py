from rest_framework import viewsets
from rest_framework import permissions
from .models import Employer, Employee, JobListing, JobApplication, Hiring
from .serializers import EmployerSerializer, EmployeeSerializer, JobListingSerializer, JobApplicationSerializer, HiringSerializer
from .permissions import IsEmployer, IsEmployee, IsAdmin
from django.shortcuts import render


# Entry Site
def index(request):
    return render(request, 'index.html')


# Employer Viewsets
class EmployerViewSet(viewsets.ModelViewSet):
    """
    ## Employer API
    Use this endpoint to:
    
    - **List all employers**.
    - **Create new employers** (requires authentication and employer role).
    - **Retrieve a specific employer**.
    - **Update an employer** (requires authentication and employer role).
    - **Delete an employer** (requires authentication and employer role).
    
    ### Fields:
    - `name`: Employer's name.
    - `company`: Company associated with the employer.
    - `email`: Employer's contact email.
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer, IsAdmin]


# Employee Viewset
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ## Employee API
    Use this endpoint to:
    
    - **List all employees**.
    - **Create new employees** (requires authentication and employee role).
    - **Retrieve a specific employee**.
    - **Update an employee** (requires authentication and employee role).
    - **Delete an employee** (requires authentication and employee role).
    
    ### Fields:
    - `name`: Employee's name.
    - `resume`: Employee's resume or CV.
    - `skills`: A list of skills the employee possesses.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee, IsAdmin]


# Job Listing Views
class JobListingViewSet(viewsets.ModelViewSet):
    """
    ## Job Listing API
    Use this endpoint to:
    
    - **List all available job listings**.
    - **Create new job listings** (requires authentication and employer role).
    - **Retrieve a specific job listing**.
    - **Update a job listing** (requires authentication and employer role).
    - **Delete a job listing** (requires authentication and employer role).
    
    ### Fields:
    - `title`: Job title.
    - `description`: Job description.
    - `skill_set`: Required skills for the job.
    """
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer, IsAdmin]


# Job Application ViewSet
class JobApplicationViewSet(viewsets.ModelViewSet):
    """
    ## Job Application API
    Use this endpoint to:
    
    - **List all job applications**.
    - **Create new job applications** (requires authentication and employee role).
    - **Retrieve a specific job application**.
    - **Update a job application** (requires authentication and employee role).
    - **Delete a job application** (requires authentication and employee role).
    
    ### Fields:
    - `job_listing`: The job being applied for.
    - `employee`: The employee applying for the job.
    - `status`: Status of the application (e.g., submitted, reviewed).
    """
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee, IsAdmin]

# Hiring ViewSet
class HiringViewSet(viewsets.ModelViewSet):
    """
    ## Hiring API
    Use this endpoint to:
    
    - **List all hiring records**.
    - **Create new hiring records** (requires authentication and employer role).
    - **Retrieve a specific hiring record**.
    - **Update a hiring record** (requires authentication and employer role).
    - **Delete a hiring record** (requires authentication and employer role).
    
    ### Fields:
    - `employer`: The employer hiring the employee.
    - `employee`: The employee being hired.
    - `job_listing`: The job associated with the hiring.
    - `hiring_date`: The date of hiring.
    """
    queryset = Hiring.objects.all()
    serializer_class = HiringSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer, IsAdmin]
