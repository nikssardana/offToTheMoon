# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoryAboutMoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('Myth', 'Myth'), ('Fact', 'Fact'), ('Story', 'Story')], max_length=10)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
            ],
        ),
    ]
