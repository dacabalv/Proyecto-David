# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0011_auto_20151202_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='foto',
            field=models.ImageField(null=True, upload_to='Viajar/static/media'),
        ),
    ]
