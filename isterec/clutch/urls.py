from django.conf.urls import url, include
from . import views as clutch_views


urlpatterns = [ 
	url(r'^$', clutch_views.home, name='home'),
	url(r'^questions/1/$', clutch_views.questions_1, name='questions_1'),
	url(r'^questions/2/$', clutch_views.questions_2, name='questions_2'),
	url(r'^upload/$', clutch_views.upload, name='upload'),
	url(r'^success/$', clutch_views.success, name='success'),
	]
