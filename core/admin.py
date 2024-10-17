from django.contrib import admin
from .models import Employee, Employer, JobListing, JobApplication, JobApplication, Hiring

# Register your models here.
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(JobListing)
admin.site.register(JobApplication)
admin.site.register(Hiring)
