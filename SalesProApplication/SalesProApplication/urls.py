"""
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

    url(r'^get_properties/(?P<agent_id>[0-9]+)/$', 'app.views.get_properties', name='get_properties'),

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
