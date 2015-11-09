"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

from .forms import SellerForm, BuyerForm, PropertyForm, AgentForm, ProgressorForm
from .models import Agent, Property

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

def add_progressor(request):
    """Renders the new page."""
    assert isinstance(request, HttpRequest)
   
    if request.method == 'POST': # If the form has been submitted...
        print("Post")
        print(request.POST)

        progressor_form = ProgressorForm(request.POST) # A form bound to the POST data        
        if progressor_form.is_valid(): # All validation rules pass
            print("Form is valid")
            progressor_form.save()
            return HttpResponseRedirect('/agents') # Redirect after POST
        else:
            print("Form/s not valid")
            print(progressor_form.errors)
    else:
        print("Get")
        progressor_form = ProgressorForm() # Initialise empty forms

    return render(
        request,
        'app/add_progressor.html',
        context_instance = RequestContext(request,
        {
            'progressor_form':progressor_form,
        })
    )

def add_agent(request):
    """Renders the new page."""
    assert isinstance(request, HttpRequest)
   
    if request.method == 'POST': # If the form has been submitted...
        print("Post")
        print(request.POST)

        agent_form = AgentForm(request.POST) # A form bound to the POST data        
        if agent_form.is_valid(): # All validation rules pass
            print("Form is valid")
            agent_form.save()
            return HttpResponseRedirect('/agents') # Redirect after POST
        else:
            print("Form/s not valid")
            print(agent_form.errors)
    else:
        print("Get")
        agent_form = AgentForm() # Initialise empty forms

    return render(
        request,
        'app/add_agent.html',
        context_instance = RequestContext(request,
        {
            'agent_form':agent_form,
        })
    )

def agent_details(request):
    """Renders the agents page."""
    assert isinstance(request, HttpRequest)
    pipeline = Property.objects.all()

    return render(
        request,
        'app/agent_details.html',
        context_instance = RequestContext(request,
        {
            'title':'Agent Details',
            'pipeline':pipeline,
            'year':datetime.now().year,
        })
    )

def agents(request):
    """Renders the agents page."""
    assert isinstance(request, HttpRequest)
    agents = Agent.objects.all()

    return render(
        request,
        'app/agents.html',
        context_instance = RequestContext(request,
        {
            'title':'Agents',
            'agents': agents
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
        seller_form = SellerForm(request.POST) # A form bound to the POST data
        buyer_form = BuyerForm(request.POST)
        agent_form = AgentForm(request.POST)
        property_form = PropertyForm(request.POST)
        progressor_form = ProgressorForm(request.POST)
        
#        property_form.agent = Agent.objects.get(id=agent_form.id)
        print(request.POST)
        if seller_form.is_valid() and buyer_form.is_valid() and property_form.is_valid() and agent_form.is_valid() and progressor_form.is_valid(): # All validation rules pass
            print("Forms are valid")
            seller_form.save()
            buyer_form.save()
            tmp_agent_form = agent_form.save() # Fake save in order to get form as an object
            agent_id = tmp_agent_form.id # Get the generated agent id
            
            print(tmp_agent_form)
            print(tmp_agent_form.id)
            print(tmp_agent_form.pk)
            print("Agent id: %s"%agent_id)
            
            
            tmp_property_form = property_form.save(commit=False) # Fake save to get form as an object
            tmp_property_form.agent = Agent.objects.get(id=agent_id) # Assign agent property using the agent id we retrieved earlier
            tmp_property_form.save()

            progressor_form.save()
            print("Forms successfully saved to database")
            return HttpResponseRedirect('/agents') # Redirect after POST
        else:
            print("Form/s not valid")
            print(seller_form.errors)
            print(buyer_form.errors)
            print(agent_form.errors)
            print(property_form.errors)
            print(progressor_form.errors)
    else:
        print("Get")
        seller_form = SellerForm() # Initialise empty forms
        buyer_form = BuyerForm()
        agent_form = AgentForm()
        property_form = PropertyForm()
        progressor_form = ProgressorForm()

    return render(
        request,
        'app/new.html',
        context_instance = RequestContext(request,
        {
            'title':'New Sale',
            'seller_form':seller_form,
            'buyer_form':buyer_form,
            'agent_form':agent_form,
            'property_form':property_form,
            'progressor_form':progressor_form,
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



