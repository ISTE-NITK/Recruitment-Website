from django.conf.urls import url, include
from . import views


urlpatterns = [ 
	url(r'^$', 'clutch.views.home', name='home'),
	url(r'^questions/1/$', 'clutch.views.questions_1', name='questions_1'),
	url(r'^questions/2/$', 'clutch.views.questions_2', name='questions_2'),
	url(r'^upload/$', 'charge.views.upload', name='upload'),
	url(r'^success/$', 'clutch.views.success', name='success'),
	]
