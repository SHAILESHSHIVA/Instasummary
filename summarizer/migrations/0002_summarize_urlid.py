# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarize',
            name='urlid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
