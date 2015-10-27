"""
Definition of models.
"""

from django.db import models

class Purchaser(models.Model):
    first_name_p_1 = models.CharField(max_length=20)
    last_name_p_1 = models.CharField(max_length=20)
    telephone_p_1 = models.IntegerField(max_length=11)
    first_name_p_2 = models.CharField(max_length=20)
    last_name_p_2 = models.CharField(max_length=20)
    telephone_p_2 = models.IntegerField(max_length=11)
    first_name_p_3 = models.CharField(max_length=20)
    last_name_p_3 = models.CharField(max_length=20)
    telephone_p_3 = models.IntegerField(max_length=11)
    first_name_p_4 = models.CharField(max_length=20)
    last_name_p_4 = models.CharField(max_length=20)
    telephone_p_4 = models.IntegerField(max_length=11)
    address_line_1 = models.CharField(max_length=20)

class Vendor(models.Model):
    first_name_v_1 = models.CharField(max_length=20)
    last_name_v_1 = models.CharField(max_length=20)
    telephone_v_1 = models.IntegerField(max_length=11)
    first_name_v_2 = models.CharField(max_length=20)
    last_name_v_2 = models.CharField(max_length=20)
    telephone_v_2 = models.IntegerField(max_length=11)
    first_name_v_3 = models.CharField(max_length=20)
    last_name_v_3 = models.CharField(max_length=20)
    telephone_v_3 = models.IntegerField(max_length=11)
    first_name_v_4 = models.CharField(max_length=20)
    last_name_v_4 = models.CharField(max_length=20)
    telephone_v_4 = models.IntegerField(max_length=11)
    address_line_1 = models.CharField(max_length=20)

class Agent(models.Model):
    address_line_1 = models.CharField(max_length=20)
    address_line_2 = models.CharField(max_length=20)
    address_line_3 = models.CharField(max_length=20)
    postcode = models.CharField(max_length=6)
    company_name = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=20)
    telephone = models.IntegerField(max_length=11)
    email_address = models.EmailField()

class Sale(models.Model):
    agreed_price = models.DecimalField(max_digits=9, decimal_places=2)
    agent_commission = models.DecimalField(max_digits=9, decimal_places=2)
    freehold_leasehold = models.DecimalField(max_digits=9, decimal_places=2)
    lease_length = models.IntegerField()
    date_agreed = models.DateField()
    date_target = models.DateField()
    required_finance = models.BooleanField()

