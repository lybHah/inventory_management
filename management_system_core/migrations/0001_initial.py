# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import management_system_core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_type', models.CharField(default=management_system_core.models.make_product_key, max_length=128)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('buy_in', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('model', models.CharField(default=b'', max_length=128, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfficeProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_type', models.CharField(default=management_system_core.models.make_product_key, max_length=128)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('buy_in', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_key', models.CharField(default=management_system_core.models.make_product_key, unique=True, max_length=32)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('total', models.IntegerField(default=0)),
                ('total_price', models.FloatField(default=0)),
            ],
        ),
    ]
