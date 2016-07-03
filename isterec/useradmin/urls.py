from django.conf.urls import url, include, patterns
from django.views.generic import ListView, DetailView
from credit.models import CreditRecData


urlpatterns = [ 
                url(r'^$', 'useradmin.views.home'),
				url(r'^login/$','django.contrib.auth.views.login', name='login', kwargs={'template_name': 'useradmin/login.html'}),
				url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout',kwargs={'next_page': '/'}),
            ]
