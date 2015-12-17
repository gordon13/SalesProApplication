# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_reminder'),
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
