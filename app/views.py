"""
Definition of views.
"""

import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.template import RequestContext
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from datetime import datetime

from .forms import SellerForm, BuyerForm, PropertyForm, AgentForm, ProgressorForm, MilestoneForm, ProfileForm
from .models import Agent, Property, Milestone, Buyer, Seller, UserProfile

# Entry point of application. Redirects user to appropriate page
def user_redirect(request):
    user = request.user
    assert isinstance(request, HttpRequest)
    if user.is_authenticated():
        if user.profile.user_type != 3 and user.profile.user_type is not None:
            return HttpResponseRedirect('/home') # Redirect after POST
        else:
            return HttpResponseRedirect('/milestones') # Redirect after POST
    else:
        return HttpResponseRedirect('/login') # Redirect after POST

@login_required
def home(request):
    """Renders the dashboard."""
    assert isinstance(request, HttpRequest)

    properties = Property.objects.filter(agent__user_id=request.user.id)
    milestones = Milestone.objects.all()
    reminders = []

    # dynamically create query to retrive the reminders/milestones
    query = Q()
    if properties and milestones:
        for property_obj in properties:
            query &= Q(property_obj_id=property_obj.id)
    reminders = milestones.filter(query)

    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Main Dashboard',
            'properties':properties,
            'reminders':reminders,
            'year':datetime.now().year,
        })
    )

@login_required
def user_profile(request):
    """Renders the user_profile."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST': # If the form has been submitted...
        print("Post")
        print(request.POST)

        profile_form = ProfileForm(request.POST, instance=request.user.profile)     
        if profile_form.is_valid():
            print("Form is valid")
            profile_form.save()
            return HttpResponseRedirect('/user_profile')
        else:
            print("Form/s not valid")
            print(profile_form.errors)
    else:
        print("Get")
        profile_form = ProfileForm(instance=request.user.profile)

    return render(
        request,
        'app/user_profile.html',
        context_instance = RequestContext(request,
        {
            'title':'User profile',
            'profile_form':profile_form,

        })
    )


@login_required
@user_passes_test(lambda u: u.profile.user_type == 0, login_url='/login')
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

@login_required
@user_passes_test(lambda u: u.profile.user_type == 0, login_url='/login')
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

@login_required
@user_passes_test(lambda u: u.profile.user_type == 1, login_url='/login')
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

@login_required
@user_passes_test(lambda u: u.profile.user_type == 0, login_url='/login')
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

@login_required
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

@login_required
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

@login_required
@user_passes_test(lambda u: u.profile.user_type == 1, login_url='/login')
def property(request, property_id):
    """Renders the property page."""
    assert isinstance(request, HttpRequest)

    milestones = Property.objects.get(pk=property_id).milestones
    if request.method == 'POST': # If the form has been submitted...
        print("Post")
        #seller_form = SellerForm(request.POST) # A form bound to the POST data
        milestones_form = MilestoneForm(request.POST) # A form bound to the POST data

        print(request.POST)
        if seller_form.is_valid(): # All validation rules pass
            print("Forms are valid")
            return HttpResponseRedirect('/property/'+property_id) # Redirect after POST
        else:
            print("Form/s not valid")
            print(milestones_form.errors)
    else:
        print("Get")
        milestones_form = MilestoneForm(instance=milestones)

    return render(
        request,
        'app/property.html',
        context_instance = RequestContext(request,
        {
            'title':'Property Information',
            'milestones_form': milestones_form,
            'property_id':property_id,
            'year':datetime.now().year,
        })
    )


@login_required
@user_passes_test(lambda u: u.profile.user_type == 1, login_url='/login')
def new(request):
    """Renders the new page."""
    assert isinstance(request, HttpRequest)
    
    #get current user. should be an agent
    user = request.user

    if request.method == 'POST': # If the form has been submitted...
        print("Post")

        seller_form = SellerForm(request.POST)
        seller_profile_form = ProfileForm(request.POST, prefix='seller_profile') # A form bound to the POST data
        user_seller_form = UserCreationForm(request.POST, prefix='user_seller')
        
        buyer_form = BuyerForm(request.POST)
        buyer_profile_form = ProfileForm(request.POST, prefix='buyer_profile')
        user_buyer_form = UserCreationForm(request.POST, prefix='user_buyer')

        property_form = PropertyForm(request.POST)

#        property_form.agent = Agent.objects.get(id=agent_form.id)
        if seller_profile_form.is_valid() and buyer_profile_form.is_valid() and property_form.is_valid() and user_seller_form.is_valid() and user_buyer_form.is_valid() and seller_form.is_valid() and buyer_form.is_valid(): # All validation rules pass
            print("Forms are valid")

            tmp_property_form = property_form.save(commit=False) # Fake save in order to get form as an object
            tmp_property_form.agent = Agent.objects.get(user=user)
            tmp_property_form.save() # final save to database

            #save users as objects
            tmp_user_seller_form = user_seller_form.save(commit=False)

            #set seller tables
            tmp_seller_form = seller_form.save(commit=False)
            tmp_seller_form.property_obj_id = tmp_property_form.id
            tmp_seller_form.user_id = tmp_user_seller_form.id
            tmp_seller_form.save()
            tmp_user_seller_form.save()

            #update seller user profile
            tmp_user_seller = User.objects.get(id=tmp_user_seller_form.id)
            tmp_user_seller.profile.user_type = 3

            #save users as objects
            tmp_user_buyer_form = user_buyer_form.save(commit=False)

            #set buyer tables
            tmp_buyer_form = buyer_form.save(commit=False)
            tmp_buyer_form.property_obj_id = tmp_property_form.id
            tmp_buyer_form.user_id = tmp_user_buyer_form.id
            tmp_buyer_form.save()
            tmp_user_buyer_form.save()

            #update seller user profile
            tmp_user_buyer = User.objects.get(id=tmp_user_buyer_form.id)
            tmp_user_buyer.profile.user_type = 3

            print("Forms successfully saved to database")
            return HttpResponseRedirect('/') # Redirect after POST
        else:
            print("Form/s not valid")
            print(seller_profile_form.errors)
            print(buyer_profile_form.errors)
            print(property_form.errors)

    else:
        print("Get")
        seller_form = SellerForm()
        seller_profile_form = ProfileForm(prefix='seller_profile') # Initialise empty forms
        user_seller_form = UserCreationForm(prefix='user_seller')

        buyer_form = BuyerForm()
        buyer_profile_form = ProfileForm(prefix='buyer_profile')
        user_buyer_form = UserCreationForm(prefix='user_buyer')

        property_form = PropertyForm()

    return render(
        request,
        'app/new.html',
        context_instance = RequestContext(request,
        {
            'title':'New Sale',

            'seller_form':seller_form,
            'seller_profile_form':seller_profile_form,
            'user_seller_form':user_seller_form,

            'buyer_form':buyer_form,
            'buyer_profile_form':buyer_profile_form,
            'user_buyer_form':user_buyer_form,

            'property_form':property_form,
            'year':datetime.now().year,
        })
    )

@login_required
@user_passes_test(lambda u: u.profile.user_type == 3, login_url='/login')
def milestones(request):
    """Renders the milestones page."""
    assert isinstance(request, HttpRequest)
    print("Milestones view")

    """Check if user is a buyer or a seller. User should only be either one. Never both"""
    buyer = Buyer.objects.filter(user_id=request.user.id).first() # Returns object, or None
    seller = Seller.objects.filter(user_id=request.user.id).first() # Returns object, or None
    #property_id = buyer.property_obj_id
    
    # If either seller or buyer is not None, then get the id of which ever is valid
    if (buyer is not None and buyer.property_obj is not None):
        property_obj = buyer.property_obj
        property_id = property_obj.id
    elif (seller is not None and seller.property_obj is not None):
        property_obj = seller.property_obj
        property_id = property_obj.id
    else:
        property_id = None
        property_obj = None
        milestones = None
        print("Buyer/Seller for user not found")
    
    if property_id is not None and milestones is not None:
        milestones = get_object_or_404(Property, pk=property_id).milestones

        """
        Calculate percentage complete by summing the 'true' values
        """
        milestones_arr  = [milestones.milestone1, milestones.milestone2, milestones.milestone3, milestones.milestone4, milestones.milestone5]
        done            = sum(milestones_arr)
        percentage      = done / len(milestones_arr) * 100
    else:
        percentage = 0

    return render(
        request,
        'app/milestones.html',
        context_instance = RequestContext(request,
        {
            'title':'Milestones',
            'property':property_obj,
            'milestones':milestones,
            'percentage':percentage,
            'year':datetime.now().year,
        })
    )

@login_required 
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

@login_required
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

@login_required
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






""" 
Non page based views. e.g. return data like the properties etc
"""

@login_required
def get_properties(request, agent_id):
    """Renders the pipeline page."""
    if request.method == 'GET':
        properties = Property.objects.filter(agent=agent_id)
        html = render_to_string('app/components/agent_properties_list.html', {'properties': properties})
        return HttpResponse(html)
    else:
        return HttpResponse(
            json.dumps({"status": "success", "message":"Got properties"}),
            content_type="application/json"
        )

@login_required
def update_milestones(request, property_id):
    """Renders the pipeline page."""
    if request.method == 'POST':
        """ 
        Need to get the current milestones object of the property (even if it is currently empty).
        And then we can feed that into the modelForm along with the POST data to update the data for those milestones
        """
        current_milestones = Milestone.objects.get(property_obj__id=property_id) # milestones for the property
        milestone_form = MilestoneForm(request.POST, instance=current_milestones) # A form bound to the POST data AND the current milestones of the property       

        if milestone_form.is_valid(): # All validation rules pass
            print("Form is valid")
            form = milestone_form.save()
            return HttpResponse(
                json.dumps({"status": "success", "message":"Milestones updated"}),
                content_type="application/json"
            )
        else: #validation fails
            print("Form/s not valid")
            print(milestone_form.errors)
            return HttpResponse(
                json.dumps({"status": "failure", "message":"Milestones NOT updated..."}),
                content_type="application/json"
            )

        return HttpResponse(html)
