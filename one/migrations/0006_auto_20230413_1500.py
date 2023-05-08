# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-04-13 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0005_auto_20230413_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('people', models.ManyToManyField(to='one.People')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='one.Grade'),
        ),
    ]