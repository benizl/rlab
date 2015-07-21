# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpga_reserve', '0006_allocation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='backend',
            name='board_type',
            field=models.CharField(default='DE2-115', max_length=40),
            preserve_default=False,
        ),
    ]
