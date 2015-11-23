# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_auto_20151121_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='_property',
            new_name='property_obj',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='_property',
            new_name='property_obj',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='_property',
            new_name='property_obj',
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agent',
            name='progressor',
            field=models.ForeignKey(blank=True, null=True, to='app.Progressor', default=0),
        ),
    ]
