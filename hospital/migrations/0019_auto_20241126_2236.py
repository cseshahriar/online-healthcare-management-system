# Generated by Django 3.2.15 on 2024-11-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20241126_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='license_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='valid_license_document',
            field=models.FileField(blank=True, null=True, upload_to='license_document/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='zoom_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
