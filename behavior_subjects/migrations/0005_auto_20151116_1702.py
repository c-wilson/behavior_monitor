# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0004_auto_20151116_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='lickgraceperiod',
            field=models.IntegerField(verbose_name='Lick Grace Period', blank=True, default=0),
        ),
        migrations.AddField(
            model_name='session',
            name='odorset_name',
            field=models.CharField(verbose_name='Odorset name', blank=True, default='', max_length=32),
        ),
        migrations.AddField(
            model_name='session',
            name='protocol_name',
            field=models.CharField(verbose_name='Protocol Name', blank=True, default='', max_length=32),
        ),
        migrations.AddField(
            model_name='session',
            name='rig',
            field=models.CharField(verbose_name='Rig', blank=True, default='', max_length=10),
        ),
    ]
