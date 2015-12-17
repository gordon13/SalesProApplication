# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151028_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('address_line_1', models.CharField(max_length=20, blank=True)),
                ('address_line_2', models.CharField(max_length=20, blank=True)),
                ('address_line_3', models.CharField(max_length=20, blank=True)),
                ('postcode', models.CharField(max_length=6, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='agent',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='address_line_3',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='postcode',
        ),
        migrations.AlterField(
            model_name='agent',
            name='company_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='contact_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='email_address',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='telephone_agent',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='address_line_1',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_1',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_3',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='first_name_p_4',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_1',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_3',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='last_name_p_4',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_1',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_2',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_3',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='telephone_p_4',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='agent_commission',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sale',
            name='agreed_price',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_agreed',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_target',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='freehold_leasehold',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sale',
            name='lease_length',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address_line_1',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='first_name_v_1',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='first_name_v_2',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='first_name_v_3',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='first_name_v_4',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='last_name_v_1',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='last_name_v_2',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='last_name_v_3',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='last_name_v_4',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='telephone_v_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='telephone_v_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='telephone_v_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='telephone_v_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='agent',
            field=models.ForeignKey(to='app.Agent'),
        ),
    ]
