# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank='True', upload_to='profile_image'),
        ),
    ]
