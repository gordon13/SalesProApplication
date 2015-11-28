"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget

from .models import Seller, Buyer, Property, Agent, Progressor, Milestone

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ['id', 'property']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        exclude = ['id', 'property']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class ProgressorForm(forms.ModelForm):
    class Meta:
        model = Progressor
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if self.fields[field].__class__.__name__ == "DateTimeField":
                self.fields[field].widget = DateTimeWidget( usel10n = True)
            elif self.fields[field].__class__.__name__ == "BooleanField":
                self.fields[field].widget.attrs.update({
                    'class': 'boolean-field'
                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        exclude = ['id']
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if self.fields[field].__class__.__name__ == "DateTimeField":
                self.fields[field].widget = DateTimeWidget( usel10n = True)
            elif self.fields[field].__class__.__name__ == "CharField":
                self.fields[field].widget.attrs.update({
                    'rows': '3'
                })
            elif self.fields[field].__class__.__name__ == "BooleanField":
                self.fields[field].widget.attrs.update({
                    'class': 'boolean-field'
                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
