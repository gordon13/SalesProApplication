# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20151123_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('reminders_message', models.TextField(max_length=200, null=True, blank=True)),
                ('reminders_date', models.DateTimeField(null=True, blank=True)),
                ('property_obj', models.ForeignKey(to='app.Property', blank=True, null=True)),
            ],
        ),
    ]
