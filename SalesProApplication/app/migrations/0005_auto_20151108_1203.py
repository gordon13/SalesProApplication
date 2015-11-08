# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151108_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='freehold_leasehold',
            new_name='freehold',
        ),
        migrations.RemoveField(
            model_name='purchaser',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='purchaser',
            name='first_name_p_4',
        ),
        migrations.RemoveField(
            model_name='purchaser',
            name='last_name_p_4',
        ),
        migrations.RemoveField(
            model_name='purchaser',
            name='telephone_p_4',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='first_name_v_4',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='last_name_v_4',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='telephone_v_4',
        ),
        migrations.AddField(
            model_name='sale',
            name='leasehold',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=9, blank=True),
        ),
    ]
