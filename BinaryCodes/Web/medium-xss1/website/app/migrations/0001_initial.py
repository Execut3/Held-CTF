# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 04:57
from __future__ import unicode_literals

import app.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='باید شامل حرف، عدد و کاراکترهای @ . + - _  بوده و نباید تعداد کاراکترها بیش از ۳۰ باشد.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Enter a valid username.', 'invalid')], verbose_name='نام کاربری')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='آدرس ایمیل')),
                ('is_staff', models.BooleanField(default=False, help_text='نشان می\u200cدهد که آیا این کاربر می\u200cتواند وارد این وبگاه مدیریت شود یا خیر.', verbose_name='وضعیت کارمندی')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Deselect this instead of deleting accounts.', verbose_name='فعال')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ پیوستن')),
                ('receive_newsletter', models.BooleanField(default=False, verbose_name='receive newsletter')),
                ('avatar', models.ImageField(blank=True, max_length=1500, null=True, upload_to=app.models.avatar_images_upload_address)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
            },
        ),
    ]