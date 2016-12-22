# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0008_session_exh_inh_delay'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='laser_delay_actual',
            field=models.IntegerField(null=True, verbose_name='Laser delay calculated', default=0),
        ),
    ]
