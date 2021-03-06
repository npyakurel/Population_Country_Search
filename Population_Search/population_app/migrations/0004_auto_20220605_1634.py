# Generated by Django 3.2.13 on 2022-06-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('population_app', '0003_city_populationmodule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='populationmodule',
            name='age_group',
            field=models.CharField(choices=[('Old', 'Old'), ('Young', 'Young'), ('Child', 'Child')], max_length=10),
        ),
        migrations.AlterField(
            model_name='populationmodule',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]
