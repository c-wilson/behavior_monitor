# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0009_trial_laser_delay_actual'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouse',
            name='active',
            field=models.BooleanField(verbose_name='Active', default=True),
        ),
    ]
