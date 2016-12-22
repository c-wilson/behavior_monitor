# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import behavior_subjects.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTrial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trial_num', models.IntegerField(verbose_name=b'Trial Number')),
                ('result', models.IntegerField(verbose_name=b'Result')),
            ],
        ),
        migrations.CreateModel(
            name='Mice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('investigator', models.CharField(max_length=35, verbose_name=b'Investigator name')),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mouse_number', models.IntegerField(unique=True, verbose_name=b'Mouse Number')),
                ('surgery_date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Surgery Date', blank=True)),
                ('dob', models.DateField(default=django.utils.timezone.now, verbose_name=b'Date of birth', blank=True)),
                ('sex', models.CharField(default=b'', max_length=1, blank=True, choices=[(b'M', b'male'), (b'F', b'female')])),
                ('date_added', models.DateField(default=django.utils.timezone.now, verbose_name=b'Date added to database')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_num', models.CharField(max_length=4)),
                ('run_dtg', models.DateTimeField(verbose_name=b'Run DTG')),
                ('added_dtg', models.DateTimeField(verbose_name=b'Date added')),
                ('file', models.FileField(upload_to=behavior_subjects.utils.mouse_path, blank=True)),
                ('mouse', models.ForeignKey(to='behavior_subjects.Mouse')),
            ],
        ),
        migrations.AddField(
            model_name='basetrial',
            name='session',
            field=models.ForeignKey(to='behavior_subjects.Session'),
        ),
    ]
