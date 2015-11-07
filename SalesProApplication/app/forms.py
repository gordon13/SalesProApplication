"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from .models import Vendor, Purchaser, Agent, Sale

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = ['id']

class PurchaserForm(forms.ModelForm):
    class Meta:
        model = Purchaser
        exclude = ['id']

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        exclude = ['id']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['id']