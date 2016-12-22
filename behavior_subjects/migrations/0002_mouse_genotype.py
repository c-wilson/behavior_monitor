# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouse',
            name='genotype',
            field=models.CharField(default=b'Wild Type', max_length=100, verbose_name=b'Genotype', blank=True),
        ),
    ]
