# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='viajes',
            new_name='Viaje',
        ),
    ]
