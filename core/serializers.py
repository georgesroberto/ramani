from rest_framework import serializers
from .models import Profile, Employer, Employee, JobListing, JobApplication, Hiring


# Serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'role']


# Serializer for Employer model
class EmployerSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()

    class Meta:
        model = Employer
        fields = ['user', 'company_name', 'company_description']


# Serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()

    class Meta:
        model = Employee
        fields = ['user', 'resume', 'skills', 'job_preference', 'experience']

    def get_resume_url(self, obj):
        request = self.context.get('request')  # Access the request object
        if obj.resume:
            return request.build_absolute_uri(obj.resume.url)  # Construct the full URL
        return None


# Serializer for JobListing model
class JobListingSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer()

    class Meta:
        model = JobListing
        fields = ['employer', 'title', 'description', 'skill_set', 'job_type', 'salary_range', 'is_open']


# Serializer for JobApplication model
class JobApplicationSerializer(serializers.ModelSerializer):
    job_listing = JobListingSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = JobApplication
        fields = ['job_listing', 'employee', 'cover_letter', 'date_applied']


# Serializer for Hiring model
class HiringSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer()
    employee = EmployeeSerializer()
    job_listing = JobListingSerializer()

    class Meta:
        model = Hiring
        fields = ['employer', 'employee', 'job_listing', 'date_hired']
