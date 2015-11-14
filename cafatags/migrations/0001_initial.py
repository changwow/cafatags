# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Txt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=13)),
                ('subTitle', models.CharField(max_length=17)),
                ('txt', models.TextField(max_length=140)),
                ('tag', models.ForeignKey(to='cafatags.Tags')),
            ],
        ),
    ]
