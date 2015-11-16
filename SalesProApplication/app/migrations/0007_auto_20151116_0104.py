# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20151109_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('milestone1', models.BooleanField(default=False)),
                ('milestone2', models.BooleanField(default=False)),
                ('milestone3', models.BooleanField(default=False)),
                ('milestone4', models.BooleanField(default=False)),
                ('milestone5', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(choices=[('0', 'Manager'), ('1', 'Agent'), ('2', 'Progressor'), ('3', 'Basic')], blank=True, null=True)),
                ('first_name', models.CharField(null=True, blank=True, max_length=20)),
                ('last_name', models.CharField(null=True, blank=True, max_length=20)),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('email_address', models.EmailField(null=True, blank=True, max_length=254)),
                ('company_name', models.CharField(null=True, blank=True, max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='date_agreed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='date_target',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='milestone',
            name='property',
            field=models.OneToOneField(to='app.Property'),
        ),
    ]
