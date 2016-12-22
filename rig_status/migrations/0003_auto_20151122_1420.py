# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rig_status', '0002_auto_20151122_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rig',
            name='last_heartbeat',
            field=models.DateTimeField(blank=True, verbose_name='Last heartbeat', default=datetime.datetime(2015, 11, 22, 19, 20, 41, 735343, tzinfo=utc)),
        ),
    ]
