from django.conf.urls import url, include
from . import views as civil_views


urlpatterns = [ 
	url(r'^$', civil_views.home, name='home'),
	url(r'^questions/1/$', civil_views.questions_1, name='questions_1'),
	url(r'^success/$', civil_views.success, name='success'),
	]
