"""
Definition of models.
"""

from django.db import models

class Progressor(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone = models.IntegerField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    
    def __unicode__(self):
        return (self.first_name + " " + self.last_name)

class Agent(models.Model):
    progressor = models.ForeignKey(Progressor, default=0)
    company_name = models.CharField(blank=True, null=True, max_length=20)
    contact_first_name = models.CharField(blank=True, null=True, max_length=20)
    contact_last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone_agent = models.IntegerField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    
    def __unicode__(self):
        return (self.contact_first_name + " " + self.contact_last_name)

class Property(models.Model):
    agent = models.ForeignKey(Agent)   
    address_line_1 = models.CharField(blank=True, null=True, max_length=20)
    address_line_2 = models.CharField(blank=True, null=True, max_length=20)
    address_line_3 = models.CharField(blank=True, null=True, max_length=20)
    postcode = models.CharField(blank=True, null=True, max_length=6)
    
    agreed_price = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    agent_commission = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    freehold = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    leasehold = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    lease_length = models.IntegerField(blank=True, null=True)
    date_agreed = models.DateField(blank=True, null=True)
    date_target = models.DateField(blank=True, null=True)
    required_finance = models.BooleanField(blank=True, default=False)
    
    def __unicode__(self):
        return ("Property: %s, %s, %s, %s. Agent: %s"%(self.address_line_1, self.address_line_2, self.address_line_3, postcode, agent,))

class Seller(models.Model):
    property = models.ForeignKey(Property)
    first_name = models.CharField(blank=True, null=True, max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return ("Seller: %s, %s. Property: %s"%(self.first_name, self.last_name, self.address_line_1))

class Buyer(models.Model):
    property = models.ForeignKey(Property)
    first_name = models.CharField(blank=True, null=True, max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return ("Buyer: %s, %s. Property: %s"%(self.first_name, self.last_name, self.address_line_1))