# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rig_status', '0005_auto_20160105_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rig',
            name='last_heartbeat',
            field=models.DateTimeField(blank=True, verbose_name='Last heartbeat', default=django.utils.timezone.now),
        ),
    ]
