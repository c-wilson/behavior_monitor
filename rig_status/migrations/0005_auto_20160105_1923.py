# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rig_status', '0004_auto_20151125_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rig',
            name='last_heartbeat',
            field=models.DateTimeField(blank=True, verbose_name='Last heartbeat', default=datetime.datetime(2016, 1, 6, 0, 23, 13, 268412, tzinfo=utc)),
        ),
    ]
