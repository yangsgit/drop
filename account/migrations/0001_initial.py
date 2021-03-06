# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-14 08:36
from __future__ import unicode_literals

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=3000)),
                ('portrait', models.ImageField(upload_to=account.models.Profile.portrait_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backgroundImage', models.ImageField(default=None, upload_to=account.models.ThemeStyle.bgImage_path)),
                ('typography_style', models.CharField(choices=[('Dark', 'dark'), ('Light', 'light')], default='dark', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='setting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
