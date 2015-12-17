# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151108_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Progressor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Purchaser',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='contact_name',
            new_name='contact_first_name',
        ),
        migrations.AddField(
            model_name='agent',
            name='contact_last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='agent_commission',
            field=models.DecimalField(blank=True, max_digits=9, null=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='property',
            name='agreed_price',
            field=models.DecimalField(blank=True, max_digits=9, null=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='property',
            name='date_agreed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='date_target',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='freehold',
            field=models.DecimalField(blank=True, max_digits=9, null=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='property',
            name='lease_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='leasehold',
            field=models.DecimalField(blank=True, max_digits=9, null=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='property',
            name='required_finance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seller',
            name='property',
            field=models.ForeignKey(to='app.Property'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='property',
            field=models.ForeignKey(to='app.Property'),
        ),
        migrations.AddField(
            model_name='agent',
            name='progressor',
            field=models.ForeignKey(to='app.Progressor', default=0),
        ),
    ]
