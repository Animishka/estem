# Generated by Django 3.1.4 on 2021-05-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20210430_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userappointment',
            name='date_appointment',
            field=models.DateTimeField(help_text='choose the date appointment', verbose_name='Date appointment (for example: 2021-07-15 14:30:00)'),
        ),
    ]