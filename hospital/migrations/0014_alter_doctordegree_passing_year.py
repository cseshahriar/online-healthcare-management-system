# Generated by Django 3.2.15 on 2024-10-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_alter_doctordegree_passing_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordegree',
            name='passing_year',
            field=models.CharField(max_length=4, verbose_name='Year of Awarded'),
        ),
    ]