# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151108_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='company_name',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='contact_name',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='email_address',
            field=models.EmailField(null=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='telephone_agent',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_line_1',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_line_2',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_line_3',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='postcode',
            field=models.CharField(null=True, max_length=6, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='address_line_1',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_1',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_2',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_3',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_4',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_1',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_2',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_3',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_4',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_2',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_3',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_4',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='agent_commission',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=9, blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='agreed_price',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=9, blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_agreed',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_target',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='freehold_leasehold',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=9, blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='lease_length',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
