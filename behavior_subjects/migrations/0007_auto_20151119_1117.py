# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0006_auto_20151116_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='bad',
            field=models.BooleanField(default=False, verbose_name='Bad Session'),
        ),
        migrations.AddField(
            model_name='session',
            name='notes',
            field=models.TextField(blank=True, default='', verbose_name='Session Notes'),
        ),
    ]
