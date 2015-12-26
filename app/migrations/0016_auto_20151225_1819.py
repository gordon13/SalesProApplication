# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0015_auto_20151123_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='contact_first_name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='contact_last_name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='telephone_agent',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='progressor',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='progressor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='progressor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='progressor',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='email',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='telephone',
        ),
        migrations.AddField(
            model_name='progressor',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
