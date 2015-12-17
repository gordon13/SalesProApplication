# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line_1', models.CharField(max_length=20)),
                ('address_line_2', models.CharField(max_length=20)),
                ('address_line_3', models.CharField(max_length=20)),
                ('postcode', models.CharField(max_length=6)),
                ('company_name', models.CharField(max_length=20)),
                ('contact_name', models.CharField(max_length=20)),
                ('telephone_agent', models.IntegerField(max_length=11)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Purchaser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name_p_1', models.CharField(max_length=20)),
                ('last_name_p_1', models.CharField(max_length=20)),
                ('telephone_p_1', models.IntegerField(max_length=11)),
                ('first_name_p_2', models.CharField(max_length=20)),
                ('last_name_p_2', models.CharField(max_length=20)),
                ('telephone_p_2', models.IntegerField(max_length=11)),
                ('first_name_p_3', models.CharField(max_length=20)),
                ('last_name_p_3', models.CharField(max_length=20)),
                ('telephone_p_3', models.IntegerField(max_length=11)),
                ('first_name_p_4', models.CharField(max_length=20)),
                ('last_name_p_4', models.CharField(max_length=20)),
                ('telephone_p_4', models.IntegerField(max_length=11)),
                ('address_line_1', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agreed_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('agent_commission', models.DecimalField(max_digits=9, decimal_places=2)),
                ('freehold_leasehold', models.DecimalField(max_digits=9, decimal_places=2)),
                ('lease_length', models.IntegerField()),
                ('date_agreed', models.DateField()),
                ('date_target', models.DateField()),
                ('required_finance', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name_v_1', models.CharField(max_length=20)),
                ('last_name_v_1', models.CharField(max_length=20)),
                ('telephone_v_1', models.IntegerField(max_length=11)),
                ('first_name_v_2', models.CharField(max_length=20)),
                ('last_name_v_2', models.CharField(max_length=20)),
                ('telephone_v_2', models.IntegerField(max_length=11)),
                ('first_name_v_3', models.CharField(max_length=20)),
                ('last_name_v_3', models.CharField(max_length=20)),
                ('telephone_v_3', models.IntegerField(max_length=11)),
                ('first_name_v_4', models.CharField(max_length=20)),
                ('last_name_v_4', models.CharField(max_length=20)),
                ('telephone_v_4', models.IntegerField(max_length=11)),
                ('address_line_1', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
