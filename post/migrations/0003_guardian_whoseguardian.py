# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-19 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190719_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='whoseguardian',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='post.Student'),
            preserve_default=False,
        ),
    ]