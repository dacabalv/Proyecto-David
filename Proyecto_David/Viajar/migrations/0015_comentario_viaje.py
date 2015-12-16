# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0014_auto_20151203_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='viaje',
            field=models.ForeignKey(to='Viajar.Viaje', default=1),
        ),
    ]
