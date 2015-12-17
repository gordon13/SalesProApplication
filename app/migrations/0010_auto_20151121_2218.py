# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151121_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='property',
            new_name='_property',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='property',
            new_name='_property',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='property',
            new_name='_property',
        ),
    ]
