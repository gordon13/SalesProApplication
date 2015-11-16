"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

from .forms import SellerForm, BuyerForm, PropertyForm, AgentForm, ProgressorForm
from .models import Agent, Property, Milestone

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    print(request.user)
    print(request.user.profile)
    properties = Property.objects.all()

    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Main Dashboard',
            'properties':properties,
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

def agent_details(request, agent_id):
    """Renders the agents page."""
    assert isinstance(request, HttpRequest)
    agent = get_object_or_404(Agent, pk=agent_id)
    pipeline = Property.objects.filter(agent=agent.id)

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
def property(request, property_id):
    """Renders the property page."""
    assert isinstance(request, HttpRequest)

    milestones = Property.objects.get(pk=property_id).milestones

    return render(
        request,
        'app/property.html',
        context_instance = RequestContext(request,
        {
            'title':'Property Information',
            'property':property_id,
            'milestones':milestones,
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
        property_form = PropertyForm(request.POST)
        
#        property_form.agent = Agent.objects.get(id=agent_form.id)
        print(request.POST)
        if seller_form.is_valid() and buyer_form.is_valid() and property_form.is_valid(): # All validation rules pass
            print("Forms are valid")

            property_obj = property_form.save() # Fake save in order to get form as an object
            print(property_obj.id)
            print(property_obj.pk)
            tmp_seller_form = seller_form.save(commit=False)
            tmp_seller_form.property = property_obj
            
            tmp_buyer_form = buyer_form.save(commit=False)
            tmp_buyer_form.property = property_obj
           
            print(request.POST)

            property_form.save() # Fake save to get form as an object
            tmp_seller_form.save()
            tmp_buyer_form.save()
           

            print("Forms successfully saved to database")
            return HttpResponseRedirect('/agents') # Redirect after POST
        else:
            print("Form/s not valid")
            print(seller_form.errors)
            print(buyer_form.errors)
            print(property_form.errors)

    else:
        print("Get")
        seller_form = SellerForm() # Initialise empty forms
        buyer_form = BuyerForm()
        property_form = PropertyForm()

    return render(
        request,
        'app/new.html',
        context_instance = RequestContext(request,
        {
            'title':'New Sale',
            'seller_form':seller_form,
            'buyer_form':buyer_form,
            'property_form':property_form,
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
def pipeline(request):
    """Renders the pipeline page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/pipeline.html',
        context_instance = RequestContext(request,
        {
            'title':'Pipeline',
            'year':datetime.now().year,
        })
    )



# Non page based views. e.g. return data like the properties etc

def get_properties(request, agent_id):
    """Renders the pipeline page."""
    if request.method == 'GET':
        properties = Property.objects.filter(agent=agent_id)
        html = render_to_string('app/components/agent_properties_list.html', {'properties': properties})
        return HttpResponse(html)
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )