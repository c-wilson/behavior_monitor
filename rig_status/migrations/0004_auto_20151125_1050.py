# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rig_status', '0003_auto_20151122_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='rig',
            name='vnc_ip',
            field=models.URLField(default=datetime.datetime(2015, 11, 25, 15, 50, 23, 18690, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rig',
            name='last_heartbeat',
            field=models.DateTimeField(verbose_name='Last heartbeat', blank=True, default=datetime.datetime(2015, 11, 25, 15, 49, 57, 276424, tzinfo=utc)),
        ),
    ]
