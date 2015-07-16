# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpga_reserve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backend',
            name='stream_port',
            field=models.IntegerField(default=8080),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backend',
            name='web_port',
            field=models.IntegerField(default=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='backend',
            name='ip_addr',
            field=models.GenericIPAddressField(),
        ),
    ]
