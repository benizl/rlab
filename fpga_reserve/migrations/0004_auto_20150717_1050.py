# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fpga_reserve', '0003_backend_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='duration',
        ),
        migrations.AddField(
            model_name='allocation',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 17, 0, 50, 41, 463697, tzinfo=utc), verbose_name=b'End Time'),
            preserve_default=False,
        ),
    ]
