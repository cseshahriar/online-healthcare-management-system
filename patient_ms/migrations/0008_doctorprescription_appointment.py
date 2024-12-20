# Generated by Django 3.2.15 on 2024-12-08 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_ms', '0007_alter_doctorappointment_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprescription',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_prescription', to='patient_ms.doctorappointment'),
        ),
    ]
