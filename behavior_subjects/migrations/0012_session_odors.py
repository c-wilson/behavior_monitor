# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0011_auto_20160509_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='odors',
            field=models.TextField(default='', max_length=128, verbose_name='Odors used'),
        ),
    ]
