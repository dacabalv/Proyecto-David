# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Viajar', '0005_remove_viaje_numnoches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha_salida', models.CharField(max_length=30)),
                ('fecha_regreso', models.CharField(max_length=30)),
                ('n_plazas', models.CharField(max_length=30)),
                ('codigo_reserva', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('dirección', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=9)),
                ('pais', models.CharField(max_length=15)),
                ('provincia', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='Destino',
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='Instrucciones',
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='Regreso',
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='Salida',
        ),
        migrations.AddField(
            model_name='viaje',
            name='continente',
            field=models.CharField(max_length=30, default='Africa'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='lugar',
            field=models.CharField(max_length=30, default='capital'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='pais',
            field=models.CharField(max_length=30, default='Mali'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='plazas_disponibles',
            field=models.CharField(max_length=20, default='0'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='precio',
            field=models.CharField(max_length=10, default='nulo'),
        ),
        migrations.AddField(
            model_name='viaje',
            name='tipo',
            field=models.CharField(max_length=30, default='avion'),
        ),
    ]
