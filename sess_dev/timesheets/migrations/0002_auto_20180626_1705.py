# Generated by Django 2.0.6 on 2018-06-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerecords',
            name='emp_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='timerecords',
            name='ts_effort',
            field=models.IntegerField(),
        ),
    ]
