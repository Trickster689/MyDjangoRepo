# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171002_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='logo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
