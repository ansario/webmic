# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('microscope', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microscope.Slide')),
            ],
        ),
    ]
