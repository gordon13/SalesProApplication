"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from .forms import VendorForm, PurchaserForm, AgentForm, SaleForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Main Dashboard',
            'year':datetime.now().year,
        })
    )
def agents(request):
    """Renders the agents page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/agents.html',
        context_instance = RequestContext(request,
        {
            'title':'Agent Details',
            'year':datetime.now().year,
        })
    )
def reminders(request):
    """Renders the reminders page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/reminders.html',
        context_instance = RequestContext(request,
        {
            'title':'Reminders',
            'year':datetime.now().year,
        })
    )
def exchanges(request):
    """Renders the exchanges page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/exchanges.html',
        context_instance = RequestContext(request,
        {
            'title':'Exchanges',
            'year':datetime.now().year,
        })
    )
def property(request):
    """Renders the property page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/property.html',
        context_instance = RequestContext(request,
        {
            'title':'Property Information',
            'year':datetime.now().year,
        })
    )
def new(request):
    """Renders the new page."""
    assert isinstance(request, HttpRequest)
   
    if request.method == 'POST': # If the form has been submitted...
        print("Post")
        vendor_form = VendorForm(request.POST) # A form bound to the POST data
        purchaser_form = PurchaserForm(request.POST)
        agent_form = AgentForm(request.POST)
        sale_form = SaleForm(request.POST)

        if vendor_form.is_valid() and purchaser_form.is_valid() and agent_form.is_valid() and sale_form.is_valid(): # All validation rules pass
            print("Forms are valid")
            vendor_form.save()
            purchaser_form.save()
            property_form.save()
            agent_form.save()
            sale_form.save()
            print("Forms successfully saved to database")
            return HttpResponseRedirect('/agents') # Redirect after POST
        else:
            print("Form/s not valid")
    else:
        print("Get")
        vendor_form = VendorForm() # Initialise empty forms
        purchaser_form = PurchaserForm()
        agent_form = AgentForm()
        sale_form = SaleForm()

    return render(
        request,
        'app/new.html',
        context_instance = RequestContext(request,
        {
            'title':'New Sale',
            'vendor_form':vendor_form,
            'purchaser_form':purchaser_form,
            'agent_form':agent_form,
            'sale_form':sale_form,
            'year':datetime.now().year,
        })
    )
def milestones(request):
    """Renders the milestones page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/milestones.html',
        context_instance = RequestContext(request,
        {
            'title':'Milestones',
            'year':datetime.now().year,
        })
    )
def chain(request):
    """Renders the chain page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chain.html',
        context_instance = RequestContext(request,
        {
            'title':'Chain',
            'year':datetime.now().year,
        })
    )
def report(request):
    """Renders the report page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/report.html',
        context_instance = RequestContext(request,
        {
            'title':'Report',
            'year':datetime.now().year,
        })
    )



