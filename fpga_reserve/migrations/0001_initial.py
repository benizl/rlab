# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name=b'Start Time')),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_addr', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='allocation',
            name='backend',
            field=models.ForeignKey(to='fpga_reserve.Backend'),
        ),
        migrations.AddField(
            model_name='allocation',
            name='user',
            field=models.ForeignKey(to='fpga_reserve.User'),
        ),
    ]
