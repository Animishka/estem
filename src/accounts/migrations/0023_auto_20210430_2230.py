# Generated by Django 3.1.4 on 2021-04-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20210430_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='photo',
            field=models.ImageField(blank=True, default='/photos/default.png', null=True, upload_to=''),
        ),
    ]
