# Generated by Django 3.0.8 on 2020-11-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='email address', max_length=255, unique=True, verbose_name='email address')),
                ('phone_number', models.DecimalField(decimal_places=0, help_text='telephone number', max_digits=11, unique=True, verbose_name='telephone number')),
                ('first_name', models.CharField(help_text='first name', max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, help_text='last name', max_length=100, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
