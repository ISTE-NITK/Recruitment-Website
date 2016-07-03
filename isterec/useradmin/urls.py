from django.conf.urls import url, include, patterns
from django.views.generic import ListView, DetailView
from django.contrib.auth import views as auth_views
from . import views as useradmin_views

urlpatterns = [ 
                url(r'^$', useradmin_views.home),
				url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'useradmin/login.html'}),
				url(r'^logout/$', auth_views.logout, name='logout',kwargs={'next_page': '/'}),
            ]
