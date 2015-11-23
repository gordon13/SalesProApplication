from django.contrib.auth.models import User
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
        return (self.user.username + "(" + str(ACC_TYPES[self.user_type][1]) + ")")

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Progressor(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone = models.IntegerField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return (self.first_name + " " + self.last_name)

class Agent(models.Model):
    progressor = models.ForeignKey(Progressor, default=0)
    company_name = models.CharField(blank=True, null=True, max_length=20)
    contact_first_name = models.CharField(blank=True, null=True, max_length=20)
    contact_last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone_agent = models.IntegerField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    
    def __str__(self):
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
    date_agreed = models.DateTimeField(blank=True, null=True)
    date_target = models.DateTimeField(blank=True, null=True)
    required_finance = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return ("Property: %s, %s, %s, %s. Agent: %s"%(self.address_line_1, self.address_line_2, self.address_line_3, self.postcode, self.agent,))

Property.milestones = property(lambda u: Milestone.objects.get_or_create(_property=u)[0])

class Seller(models.Model):
    user = models.ForeignKey(User, blank=True, null=True) 
    _property = models.ForeignKey(Property, blank=True, null=True)
    first_name = models.CharField(blank=True, null=True, max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return ("Seller: %s, %s. Property: %s"%(self.first_name, self.last_name, self._property.address_line_1))

class Buyer(models.Model):
    user = models.ForeignKey(User, blank=True, null=True) 
    _property = models.ForeignKey(Property, blank=True, null=True)
    first_name = models.CharField(blank=True, null=True, max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    telephone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return ("Buyer: %s, %s. Property: %s"%(self.first_name, self.last_name, self._property.address_line_1))


# Milestones
class Milestone(models.Model):
    _property = models.OneToOneField(Property)
    milestone1 = models.BooleanField(blank=True, default=False)
    milestone2 = models.BooleanField(blank=True, default=False)
    milestone3 = models.BooleanField(blank=True, default=False)
    milestone4 = models.BooleanField(blank=True, default=False)
    milestone5 = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return ("Milestones for property %s: %s"%self._property.id)

# reminders
class Reminders(models.Model):
    _property = models.OneToOneField(Property)
    reminders_message = models.TextField(blank=True, null=True, max_length=200)
    reminders_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return ("reminders for property %s: %s"%self._property.id)
