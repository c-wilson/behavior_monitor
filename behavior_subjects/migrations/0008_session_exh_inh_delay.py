# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0007_auto_20151119_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='exh_inh_delay',
            field=models.IntegerField(blank=True, verbose_name='Exh-inh delay', default=-1),
        ),
    ]
