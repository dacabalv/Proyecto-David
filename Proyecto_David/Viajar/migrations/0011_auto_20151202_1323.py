# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0010_viaje_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicion',
            name='usuarios',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
