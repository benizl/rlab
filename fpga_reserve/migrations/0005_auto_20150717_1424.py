# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpga_reserve', '0004_auto_20150717_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
