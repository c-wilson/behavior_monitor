# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0010_mouse_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='first_lick_rt_calc',
            field=models.BooleanField(verbose_name='First inh rt calculated?', default=False),
        ),
        migrations.AddField(
            model_name='trial',
            name='first_lick_correct',
            field=models.BooleanField(verbose_name='First lick correct?', default=False),
        ),
        migrations.AddField(
            model_name='trial',
            name='first_lick_rt',
            field=models.IntegerField(verbose_name='First lick reaction time', default=-1),
        ),
    ]
