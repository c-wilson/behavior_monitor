# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0005_auto_20151116_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='run_dtg',
            field=models.DateTimeField(unique=True, verbose_name='Run DTG'),
        ),
    ]
