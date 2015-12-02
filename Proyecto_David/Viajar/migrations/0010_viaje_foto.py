# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0009_edicion_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='foto',
            field=models.ImageField(null=True, upload_to='pagina/static/media'),
        ),
    ]
