from django.conf.urls import url, include
from . import views


urlpatterns = [ 
	url(r'^$', 'create.views.home', name='home'),
	url(r'^questions/1/$', 'create.views.questions_1', name='questions_1'),
	url(r'^success/$', 'create.views.success', name='success'),
	]
