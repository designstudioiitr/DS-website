# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20171221_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='text_color',
            field=models.CharField(default='#ffffff', help_text='Enter Hex Code, eg #ffffff', max_length=10),
            preserve_default=False,
        ),
    ]
