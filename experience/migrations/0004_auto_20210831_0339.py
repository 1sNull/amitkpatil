# Generated by Django 3.2.5 on 2021-08-31 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_rename_compname_experience_companyname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='companydescription',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='experience',
            name='companyname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='jobdescription',
            field=models.CharField(blank=True, max_length=2550),
        ),
    ]
