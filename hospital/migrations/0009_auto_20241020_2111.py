# Generated by Django 3.2.15 on 2024-10-20 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0008_auto_20241019_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('confirmed', 'Confirmed'), ('completed', 'Completed')], default='pending', max_length=20, verbose_name='Status')),
                ('order', models.CharField(blank=True, max_length=255, null=True, verbose_name='Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hospital_degree_createdby', to=settings.AUTH_USER_MODEL)),
                ('deleted_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_degree_deleted', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_degree_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='expertize',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='upazila',
        ),
        migrations.AddField(
            model_name='doctor',
            name='availability_days',
            field=models.TextField(help_text='Sat, Sun, Mon, Tue, Wed, Thur', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='availability_time',
            field=models.TextField(help_text='10:00 AM - 12:00 PM & 05:00 PM - 10:00 PM', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='year_of_experience',
            field=models.TextField(help_text='5', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.TextField(help_text='Ex: 2/17, Mirpur-11', null=True, verbose_name='Chamber Address'),
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='speciality',
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ManyToManyField(blank=True, related_name='specialities', to='hospital.Speciality'),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('confirmed', 'Confirmed'), ('completed', 'Completed')], default='pending', max_length=20, verbose_name='Status')),
                ('order', models.CharField(blank=True, max_length=255, null=True, verbose_name='Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hospital_subject_createdby', to=settings.AUTH_USER_MODEL)),
                ('deleted_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_subject_deleted', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_subject_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('confirmed', 'Confirmed'), ('completed', 'Completed')], default='pending', max_length=20, verbose_name='Status')),
                ('order', models.CharField(blank=True, max_length=255, null=True, verbose_name='Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('institute', models.CharField(max_length=255)),
                ('passing_year', models.CharField(max_length=4, verbose_name='Year the degree was awarded')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hospital_doctordegree_createdby', to=settings.AUTH_USER_MODEL)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor_degrees', to='hospital.degree')),
                ('deleted_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_doctordegree_deleted', to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor_degrees', to='hospital.doctor')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor_degrees', to='hospital.subject')),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_doctordegree_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
