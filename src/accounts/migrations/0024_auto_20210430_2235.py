# Generated by Django 3.1.4 on 2021-04-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20210430_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]