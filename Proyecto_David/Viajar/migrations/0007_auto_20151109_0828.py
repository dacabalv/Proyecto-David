# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Viajar', '0006_auto_20151028_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opinion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_salida', models.CharField(max_length=30)),
                ('fecha_regreso', models.CharField(max_length=30)),
                ('n_plazas', models.CharField(max_length=30)),
                ('viaje', models.ForeignKey(to='Viajar.Viaje')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('dirección', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=9)),
                ('pais', models.CharField(max_length=15)),
                ('provincia', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=15)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(to='Viajar.Usuario'),
        ),
    ]
