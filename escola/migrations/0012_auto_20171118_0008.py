# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0011_caderneta_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caderneta',
            name='atendimento',
        ),
        migrations.AddField(
            model_name='caderneta',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='classe', to='escola.Classe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='caderneta',
            name='adjuntos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='caderneta',
            name='biblias',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='caderneta',
            name='matriculados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='caderneta',
            name='presentes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='caderneta',
            name='professor',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='caderneta',
            name='visitantes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]