"""
Definition of models.
"""

from django.db import models

class Vendor(models.Model):
    first_name_v_1 = models.CharField(blank=True, null=True, max_length=20)
    last_name_v_1 = models.CharField(blank=True, null=True, max_length=20)
    telephone_v_1 = models.IntegerField(blank=True, null=True)
    first_name_v_2 = models.CharField(blank=True, null=True, max_length=20)
    last_name_v_2 = models.CharField(blank=True, null=True, max_length=20)
    telephone_v_2 = models.IntegerField(blank=True, null=True)
    first_name_v_3 = models.CharField(blank=True, null=True, max_length=20)
    last_name_v_3 = models.CharField(blank=True, null=True, max_length=20)
    telephone_v_3 = models.IntegerField(blank=True, null=True)

class Purchaser(models.Model):
    first_name_p_1 = models.CharField(blank=True, null=True, max_length=20)
    last_name_p_1 = models.CharField(blank=True, null=True, max_length=20)
    telephone_p_1 = models.IntegerField(blank=True, null=True)
    first_name_p_2 = models.CharField(blank=True, null=True, max_length=20)
    last_name_p_2 = models.CharField(blank=True, null=True, max_length=20)
    telephone_p_2 = models.IntegerField(blank=True, null=True)
    first_name_p_3 = models.CharField(blank=True, null=True, max_length=20)
    last_name_p_3 = models.CharField(blank=True, null=True, max_length=20)
    telephone_p_3 = models.IntegerField(blank=True, null=True)

class Agent(models.Model):
    company_name = models.CharField(blank=True, null=True, max_length=20)
    contact_name = models.CharField(blank=True, null=True, max_length=20)
    telephone_agent = models.IntegerField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

class Property(models.Model):
    agent = models.ForeignKey(Agent)
    address_line_1 = models.CharField(blank=True, null=True, max_length=20)
    address_line_2 = models.CharField(blank=True, null=True, max_length=20)
    address_line_3 = models.CharField(blank=True, null=True, max_length=20)
    postcode = models.CharField(blank=True, null=True, max_length=6)
    
    def __unicode__(self):
        return ("Property: %s, %s, %s, %s. Agent: %s"%(address_line_1, address_line_2, address_line_3, postcode, agent,))

class Sale(models.Model):
    agreed_price = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    agent_commission = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    freehold = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    leasehold = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    lease_length = models.IntegerField(blank=True, null=True)
    date_agreed = models.DateField(blank=True, null=True)
    date_target = models.DateField(blank=True, null=True)
    required_finance = models.BooleanField(blank=True)

