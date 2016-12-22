# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rig',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Rig')),
                ('status', models.CharField(max_length=10, verbose_name='Status')),
                ('non_responses', models.IntegerField(verbose_name='Number non-responses')),
                ('correct', models.IntegerField(verbose_name='Trials correct')),
                ('n_trials', models.IntegerField(verbose_name='Num Trials')),
                ('last_heartbeat', models.DateTimeField(verbose_name='Last heartbeat')),
            ],
        ),
    ]
