# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 04:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0005_champion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supporter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('inheritance.champion',),
        ),
    ]
