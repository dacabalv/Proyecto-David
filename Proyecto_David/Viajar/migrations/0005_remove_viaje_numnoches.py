# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0004_auto_20151022_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viaje',
            name='NumNoches',
        ),
    ]
