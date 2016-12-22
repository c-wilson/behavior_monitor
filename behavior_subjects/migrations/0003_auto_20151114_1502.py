# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import behavior_subjects.utils


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0002_mouse_genotype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trial_num', models.IntegerField(verbose_name=b'Trial Number')),
                ('result', models.IntegerField(verbose_name=b'Result')),
                ('valid', models.BooleanField(verbose_name=b'Valid response')),
                ('correct', models.BooleanField(verbose_name=b'Correct response')),
                ('odor', models.CharField(max_length=32, verbose_name=b'Odor')),
                ('odorconc', models.FloatField(verbose_name=b'Odor concentration')),
                ('laser_delay', models.IntegerField(verbose_name=b'Laser delay (ms)')),
                ('laser_intensity', models.DecimalField(verbose_name=b'Laser intensity (mW)', max_digits=10, decimal_places=7)),
                ('laser_npulses', models.IntegerField(verbose_name=b'Number laser pulses')),
            ],
        ),
        migrations.RemoveField(
            model_name='basetrial',
            name='session',
        ),
        migrations.AddField(
            model_name='session',
            name='performance',
            field=models.DecimalField(default=0.0, verbose_name=b'Session performance', max_digits=3, decimal_places=2),
        ),
        migrations.AddField(
            model_name='session',
            name='trials_correct',
            field=models.IntegerField(default=0, verbose_name=b'Trials correct'),
        ),
        migrations.AddField(
            model_name='session',
            name='valid_trials',
            field=models.IntegerField(default=0, verbose_name=b'Number trials completed'),
        ),
        migrations.AlterField(
            model_name='session',
            name='file',
            field=models.FileField(upload_to=behavior_subjects.utils.mouse_path),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_num',
            field=models.CharField(max_length=5, verbose_name=b'Session number'),
        ),
        migrations.DeleteModel(
            name='BaseTrial',
        ),
        migrations.AddField(
            model_name='trial',
            name='session',
            field=models.ForeignKey(to='behavior_subjects.Session'),
        ),
    ]
