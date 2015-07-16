# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpga_reserve', '0002_auto_20150716_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='backend',
            name='name',
            field=models.CharField(default='Backend', max_length=20),
            preserve_default=False,
        ),
    ]
