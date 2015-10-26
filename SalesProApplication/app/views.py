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
            'title':'SalesPro',
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
            'title':'Agents',
            'year':datetime.now().year,
        })
    )
def properties(request):
    """Renders the properties page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/properties.html',
        context_instance = RequestContext(request,
        {
            'title':'Properties',
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
def archive(request):
    """Renders the archive page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/archive.html',
        context_instance = RequestContext(request,
        {
            'title':'Archive',
            'year':datetime.now().year,
        })
    )
def invoice(request):
    """Renders the invoice page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/invoice.html',
        context_instance = RequestContext(request,
        {
            'title':'Invoices Due',
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
            'title':'Total Pipeline',
            'year':datetime.now().year,
        })
    )
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )


