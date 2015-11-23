# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151123_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('reminders_message', models.TextField(blank=True, null=True, max_length=200)),
                ('reminders_date', models.DateTimeField(blank=True, null=True)),
                ('property_obj', models.ForeignKey(blank=True, null=True, to='app.Property')),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='date1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='date2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='date3',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='date4',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='date5',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='message1',
            field=models.TextField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='milestone',
            name='message2',
            field=models.TextField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='milestone',
            name='message3',
            field=models.TextField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='milestone',
            name='message4',
            field=models.TextField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='milestone',
            name='message5',
            field=models.TextField(blank=True, null=True, max_length=200),
        ),
    ]
