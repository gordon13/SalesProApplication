# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20151123_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='property_obj',
        ),
        migrations.DeleteModel(
            name='Reminder',
        ),
    ]
