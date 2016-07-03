from django.conf.urls import url, include
from . import views as charge_views


urlpatterns = [ 
	url(r'^$', charge_views.home, name='home'),
	url(r'^questions/1/$', charge_views.questions_1, name='questions_1'),
	url(r'^questions/2/$', charge_views.questions_2, name='questions_2'),
	url(r'^questions/3/$', charge_views.questions_3, name='questions_3'),
	url(r'^success/$', charge_views.success, name='success'),
	]
