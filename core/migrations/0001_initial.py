# Generated by Django 5.1.2 on 2024-10-17 01:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('skills', models.TextField()),
                ('job_preference', models.CharField(max_length=255)),
                ('experience', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('skill_set', models.TextField()),
                ('job_type', models.CharField(max_length=50)),
                ('salary_range', models.CharField(blank=True, max_length=50)),
                ('is_open', models.BooleanField(default=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employer')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.TextField(blank=True)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
                ('job_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.joblisting')),
            ],
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_hired', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employer')),
                ('job_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.joblisting')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('employer', 'Employer'), ('employee', 'Employee')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]
