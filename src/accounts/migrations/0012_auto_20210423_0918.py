# Generated by Django 3.1.4 on 2021-04-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210422_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]