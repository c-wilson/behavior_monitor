# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rig_status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rig',
            name='correct',
            field=models.IntegerField(default=0, verbose_name='Trials correct', blank=True),
        ),
        migrations.AlterField(
            model_name='rig',
            name='last_heartbeat',
            field=models.DateTimeField(default=0, verbose_name='Last heartbeat', blank=True),
        ),
        migrations.AlterField(
            model_name='rig',
            name='n_trials',
            field=models.IntegerField(default=0, verbose_name='Num Trials', blank=True),
        ),
        migrations.AlterField(
            model_name='rig',
            name='non_responses',
            field=models.IntegerField(default=0, verbose_name='Number non-responses', blank=True),
        ),
        migrations.AlterField(
            model_name='rig',
            name='status',
            field=models.CharField(max_length=10, default='', verbose_name='Status', blank=True),
        ),
    ]
