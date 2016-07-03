from django.conf.urls import url, include
from . import views as civil_views


urlpatterns = [ 
	url(r'^$',civil_views.index, name='index')]
