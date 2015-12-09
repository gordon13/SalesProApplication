﻿"""
Definition of urls for SalesProApplication.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # App pages
    url(r'^home$', 'app.views.home', name='home'),
    url(r'^user_profile$', 'app.views.user_profile', name='user_profile'),
    url(r'^add_progressor$', 'app.views.add_progressor', name='add_progressor'),
    url(r'^add_agent$', 'app.views.add_agent', name='add_agent'),
    url(r'^agents$', 'app.views.agents', name='agents'),
    url(r'^agent_details/(?P<agent_id>[0-9]+)/$', 'app.views.agent_details', name='agent_details'),
    url(r'^reminders$', 'app.views.reminders', name='reminders'),
    url(r'^exchanges$', 'app.views.exchanges', name='exchanges'),
    url(r'^property/(?P<property_id>[0-9]+)/$', 'app.views.property', name='property'),
    url(r'^new$', 'app.views.new', name='new'),
    url(r'^milestones$', 'app.views.milestones', name='milestones'),
    url(r'^chain$', 'app.views.chain', name='chain'),
    url(r'^pipeline$', 'app.views.pipeline', name='pipeline'),
    url(r'^report$', 'app.views.report', name='report'),

    # used by ajax
    url(r'^get_properties/(?P<agent_id>[0-9]+)/$', 'app.views.get_properties', name='get_properties'),
    url(r'^update_milestones/(?P<property_id>[0-9]+)/$', 'app.views.update_milestones', name='update_milestones'),

    # Used to redirect the user to their respective page
    url(r'^$', 'app.views.user_redirect', name='user_redirect'),

    # Authentication
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
            'next_page': '/login',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
