from django.conf.urls import url, include
from . import views


urlpatterns = [ 
	url(r'^$', 'credit.views.home', name='home'),
	url(r'^questions/1/$', 'credit.views.questions_1', name='questions_1'),
	url(r'^success/$', 'credit.views.success', name='success'),
	]
