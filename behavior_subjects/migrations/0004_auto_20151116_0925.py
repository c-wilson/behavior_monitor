# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_subjects', '0003_auto_20151114_1502'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mice',
        ),
        migrations.AlterField(
            model_name='mouse',
            name='date_added',
            field=models.DateField(verbose_name='Date added to database', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of birth', blank=True),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='genotype',
            field=models.CharField(default='Wild Type', max_length=100, verbose_name='Genotype', blank=True),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='mouse_number',
            field=models.IntegerField(verbose_name='Mouse Number', unique=True),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='sex',
            field=models.CharField(max_length=1, default='', choices=[('M', 'male'), ('F', 'female')], blank=True),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='surgery_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Surgery Date', blank=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='added_dtg',
            field=models.DateTimeField(verbose_name='Date added'),
        ),
        migrations.AlterField(
            model_name='session',
            name='performance',
            field=models.DecimalField(max_digits=3, verbose_name='Session performance', decimal_places=2, default=0.0),
        ),
        migrations.AlterField(
            model_name='session',
            name='run_dtg',
            field=models.DateTimeField(verbose_name='Run DTG'),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_num',
            field=models.CharField(max_length=5, verbose_name='Session number'),
        ),
        migrations.AlterField(
            model_name='session',
            name='trials_correct',
            field=models.IntegerField(verbose_name='Trials correct', default=0),
        ),
        migrations.AlterField(
            model_name='session',
            name='valid_trials',
            field=models.IntegerField(verbose_name='Number trials completed', default=0),
        ),
        migrations.AlterField(
            model_name='trial',
            name='correct',
            field=models.BooleanField(verbose_name='Correct'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='laser_delay',
            field=models.IntegerField(verbose_name='Laser delay (ms)'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='laser_intensity',
            field=models.DecimalField(max_digits=10, verbose_name='Laser intensity (mW)', decimal_places=7),
        ),
        migrations.AlterField(
            model_name='trial',
            name='laser_npulses',
            field=models.IntegerField(verbose_name='Number laser pulses'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='odor',
            field=models.CharField(max_length=32, verbose_name='Odor'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='odorconc',
            field=models.FloatField(verbose_name='Odor concentration'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='result',
            field=models.IntegerField(verbose_name='Result'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='trial_num',
            field=models.IntegerField(verbose_name='Trial Number'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='valid',
            field=models.BooleanField(verbose_name='Valid'),
        ),
    ]
