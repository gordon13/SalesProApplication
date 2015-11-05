"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

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
    return render(
        request,
        'app/new.html',
        context_instance = RequestContext(request,
        {
            'title':'New Sale',
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



