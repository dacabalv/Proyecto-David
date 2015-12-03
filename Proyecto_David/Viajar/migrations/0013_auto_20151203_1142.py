# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0012_auto_20151203_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicion',
            name='n_plazas',
            field=models.IntegerField(max_length=30),
        ),
    ]
