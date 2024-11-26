# Generated by Django 3.2.15 on 2024-11-16 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_auto_20241027_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name_plural': 'Doctor Specialists'},
        ),
        migrations.AddField(
            model_name='symptom',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='symptoms', to='hospital.speciality'),
        ),
    ]