# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-04-13 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_auto_20230413_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.Grade')),
            ],
        ),
        migrations.AlterField(
            model_name='idcard',
            name='people',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='one.People'),
        ),
    ]