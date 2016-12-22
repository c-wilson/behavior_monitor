# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rig_status', '0006_auto_20160108_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='rig',
            name='miss_alerted',
            field=models.IntegerField(verbose_name='miss alert sent', default=0),
        ),
        migrations.AddField(
            model_name='rig',
            name='pause1',
            field=models.BooleanField(verbose_name='paused', default=False),
        ),
        migrations.AddField(
            model_name='rig',
            name='pause_alerted',
            field=models.BooleanField(verbose_name='pause alert sent', default=False),
        ),
    ]
