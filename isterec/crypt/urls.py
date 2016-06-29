from django.conf.urls import url, include
from . import views


urlpatterns = [ 
	url(r'^$', 'crypt.views.home', name='home'),
	url(r'^upload/$', 'crypt.views.upload', name='upload'),
	url(r'^success/$', 'crypt.views.success', name='success'),]
