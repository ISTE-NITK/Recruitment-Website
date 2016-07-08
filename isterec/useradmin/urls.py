from django.conf.urls import url, include, patterns
from django.views.generic import ListView, DetailView
from django.contrib.auth import views as auth_views
from . import views as useradmin_views

urlpatterns = [ 
                url(r'^$', useradmin_views.home),
				
				url(r'^crypt/$', useradmin_views.index, kwargs={'sig_name': 'Crypt'}),
				url(r'^charge/$', useradmin_views.index, kwargs={'sig_name': 'Charge'}),
				url(r'^clutch/$', useradmin_views.index, kwargs={'sig_name': 'Clutch'}),
				url(r'^create/$', useradmin_views.index, kwargs={'sig_name': 'Create'}),
				url(r'^civil/$', useradmin_views.index, kwargs={'sig_name': 'Civil'}),
				url(r'^credit/$', useradmin_views.index, kwargs={'sig_name': 'Credit'}),
				url(r'^chronicle/$', useradmin_views.index, kwargs={'sig_name': 'Chronicle'}),
				url(r'^crypt/results/$', useradmin_views.search, kwargs={'sig_name': 'crypt'}),
				url(r'^charge/results/$', useradmin_views.search, kwargs={'sig_name': 'charge'}),
				url(r'^clutch/results/$', useradmin_views.search, kwargs={'sig_name': 'clutch'}),
				url(r'^credit/results/$', useradmin_views.search, kwargs={'sig_name': 'credit'}),
				url(r'^chronicle/results/$', useradmin_views.search, kwargs={'sig_name': 'chronicle'}),
				url(r'^create/results/$', useradmin_views.search, kwargs={'sig_name': 'create'}),
				url(r'^crypt/selected/$', useradmin_views.selected, kwargs={'sig_name': 'crypt'}),
				url(r'^charge/selected/$', useradmin_views.selected, kwargs={'sig_name': 'charge'}),
				url(r'^clutch/selected/$', useradmin_views.selected, kwargs={'sig_name': 'clutch'}),
				url(r'^credit/selected/$', useradmin_views.selected, kwargs={'sig_name': 'credit'}),
				url(r'^chronicle/selected/$', useradmin_views.selected, kwargs={'sig_name': 'chronicle'}),
				url(r'^create/selected/$', useradmin_views.selected, kwargs={'sig_name': 'create'}),
				url(r'^crypt/results/detail/(?P<pk>\d+)$', useradmin_views.detailreply, kwargs={'sig_name': 'crypt'}),
				url(r'^charge/results/detail/(?P<pk>\d+)$', useradmin_views.detailreply, kwargs={'sig_name': 'charge'}),
				url(r'^credit/results/detail/(?P<pk>\d+)$', useradmin_views.detailreply, kwargs={'sig_name': 'credit'}),
				url(r'^clutch/results/detail/(?P<pk>\d+)$', useradmin_views.detailreply, kwargs={'sig_name': 'clutch'}),
				url(r'^chronicle/results/detail/(?P<pk>\d+)$', useradmin_views.detailreply, kwargs={'sig_name': 'chronicle'}),
				url(r'^create/results/detail/(?P<pk>\d+)$', useradmin_views.detailreply, kwargs={'sig_name': 'create'}),
				url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'useradmin/login.html'}),
				url(r'^logout/$', auth_views.logout, name='logout',kwargs={'next_page': '/'}),
            ]
