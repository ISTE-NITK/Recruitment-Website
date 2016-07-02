from django.conf.urls import url, include
from . import views


urlpatterns = [ 
	url(r'^$', 'charge.views.home', name='home'),
	url(r'^questions/1/$', 'charge.views.questions_1', name='questions_1'),
	url(r'^questions/2/$', 'charge.views.questions_2', name='questions_2'),
	url(r'^questions/3/$', 'charge.views.questions_3', name='questions_3'),
	url(r'^success/$', 'charge.views.success', name='success'),
	]
