# Generated by Django 3.2.15 on 2024-10-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_symptom'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_vacation_mode',
            field=models.BooleanField(default=False, verbose_name='Activate Vacation Mode'),
        ),
    ]
