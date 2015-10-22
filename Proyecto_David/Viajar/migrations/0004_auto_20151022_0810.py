# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0003_auto_20151022_0810'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Viajes',
            new_name='Viaje',
        ),
    ]
