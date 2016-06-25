from django.conf.urls import url, include
from . import views


urlpatterns = [ 
	url(r'^$', 'crypt.views.home', name='home'),]
