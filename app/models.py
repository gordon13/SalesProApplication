﻿from django.contrib.auth.models import User
from django.db import models


ACC_TYPES = (
    (0, 'Manager'),
    (1, 'Agent'),
    (2, 'Progressor'),
    (3, 'Basic'))

class UserProfile(models.Model):
    user            = models.OneToOneField(User)
    user_type       = models.IntegerField(blank=True, null=True, choices = ACC_TYPES, default=3)
    first_name      = models.CharField(blank=True, null=True, max_length=20)
    last_name       = models.CharField(blank=True, null=True, max_length=20)
    telephone       = models.IntegerField(blank=True, null=True)
    email_address   = models.EmailField(blank=True, null=True)
    company_name    = models.CharField(blank=True, null=True, max_length=20)

    def user_type_verbose(self):
        return dict(ACC_TYPES)[self.user_type]

    def __str__(self):
        return ("%s(%s)"%(self.user.username, str(ACC_TYPES[self.user_type][1])))

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Progressor(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    def __str__(self):
        return ("Progressor: %s %s"%(self.user.profile.first_name, self.user.profile.last_name))

class Agent(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    progressor = models.ForeignKey(Progressor, blank=True, null=True, default=0)
    
    def get_profile(self):
        return ("%s %s"%(self.user.profile.first_name, self.user.profile.last_name, ))

    def __str__(self):
        return ("Agent: %s %s"%(self.user.profile.first_name, self.user.profile.last_name))

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
    date_agreed = models.DateTimeField(blank=True, null=True)
    date_target = models.DateTimeField(blank=True, null=True)
    required_finance = models.BooleanField(blank=True, default=False)

    def as_dict(self):
        return {
            "id": self.id,
            "agent": self.agent.user.profile.company_name,
            "address_line_1": self.address_line_1,
            "address_line_2": self.address_line_2,
            "address_line_3": self.address_line_3,
            "postcode": self.postcode
        }

    def __str__(self):
        return ("Property: %s, %s, %s, %s. Agent: %s"%(self.address_line_1, self.address_line_2, self.address_line_3, self.postcode, self.agent,))

Property.milestones = property(lambda u: Milestone.objects.get_or_create(property_obj=u)[0])

class Seller(models.Model):
    user = models.ForeignKey(User, blank=True, null=True) 
    property_obj = models.ForeignKey(Property, blank=True, null=True)

    def __str__(self):
        return ("Seller: %s, %s. Property: %s"%(self.user.profile.first_name, self.user.profile.last_name, self.property_obj.address_line_1))

class Buyer(models.Model):
    user = models.ForeignKey(User, blank=True, null=True) 
    property_obj = models.ForeignKey(Property, blank=True, null=True)

    def __str__(self):
        return ("Buyer: %s, %s. Property: %s"%(self.user.profile.first_name, self.user.profile.last_name, self.property_obj.address_line_1))


# Milestones
class Milestone(models.Model):
    property_obj = models.OneToOneField(Property)

    milestone1 = models.BooleanField(blank=True, default=False)
    message1 = models.TextField(blank=True, null=True, max_length=200)
    date1 = models.DateTimeField(blank=True, null=True)

    milestone2 = models.BooleanField(blank=True, default=False)
    message2 = models.TextField(blank=True, null=True, max_length=200)
    date2 = models.DateTimeField(blank=True, null=True)

    milestone3 = models.BooleanField(blank=True, default=False)
    message3 = models.TextField(blank=True, null=True, max_length=200)
    date3 = models.DateTimeField(blank=True, null=True)

    milestone4 = models.BooleanField(blank=True, default=False)
    message4 = models.TextField(blank=True, null=True, max_length=200)
    date4 = models.DateTimeField(blank=True, null=True)

    milestone5 = models.BooleanField(blank=True, default=False)
    message5 = models.TextField(blank=True, null=True, max_length=200)
    date5 = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return ("Milestones for property %s"%self.property_obj.id)

