# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0017_auto_20151216_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
