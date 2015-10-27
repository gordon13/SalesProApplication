﻿"""
Definition of urls for SalesProApplication.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^agents$', 'app.views.agents', name='agents'),
    url(r'^properties$', 'app.views.properties', name='properties'),
    url(r'^property$', 'app.views.property', name='property'),
    url(r'^reminders$', 'app.views.reminders', name='reminders'),
    url(r'^new$', 'app.views.new', name='new'),
    url(r'^archive$', 'app.views.archive', name='archive'),
    url(r'^invoice$', 'app.views.invoice', name='invoice'),
    url(r'^pipeline$', 'app.views.pipeline', name='pipeline'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
