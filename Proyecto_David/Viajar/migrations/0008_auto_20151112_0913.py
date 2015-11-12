# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0007_auto_20151109_0828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='edicion',
            options={'verbose_name_plural': 'ediciones', 'verbose_name': 'edición'},
        ),
    ]
