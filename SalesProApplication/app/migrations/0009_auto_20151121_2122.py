# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151121_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='property',
            field=models.ForeignKey(to='app.Property', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='property',
            field=models.ForeignKey(to='app.Property', null=True, blank=True),
        ),
    ]
