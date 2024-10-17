from django.contrib.auth.models import User
from django.db import models


# 1. Profile Model to extend the default User model
class Profile(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('employee', 'Employee'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    # Additional common fields for both employer and employee can go here

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# 2. Employer Model
class Employer(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField(blank=True)

    def __str__(self):
        return self.company_name


# 3. Employee Model
class Employee(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField()
    job_preference = models.CharField(max_length=255)
    experience = models.TextField(blank=True)  # Optional work experience

    def __str__(self):
        return f"{self.user.user.username}'s Profile"


# 4. JobListing Model
class JobListing(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    skill_set = models.TextField()
    job_type = models.CharField(max_length=50)  # e.g., full-time, part-time
    salary_range = models.CharField(max_length=50, blank=True)
    is_open = models.BooleanField(default=True)  # To track if the job is still open

    def __str__(self):
        return self.title


# 5. JobApplication Model
class JobApplication(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True)  # Optional cover letter
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.user.user.username} applied for {self.job_listing.title}"


# 6. Hiring Model
class Hiring(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    date_hired = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.user.user.username} hired by {self.employer.company_name}"
