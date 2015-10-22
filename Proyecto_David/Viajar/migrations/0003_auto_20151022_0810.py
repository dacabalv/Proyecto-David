# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0002_auto_20151021_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Destino', models.CharField(max_length=30)),
                ('Instrucciones', models.TextField()),
                ('Salida', models.DateTimeField()),
                ('Regreso', models.DateTimeField()),
                ('NumNoches', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Viaje',
        ),
    ]
