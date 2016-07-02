from django.conf.urls import url, include
from . import views


urlpatterns = [ 
	url(r'^$', 'chronicle.views.home', name='home'),
	url(r'^questions/1/$', 'chronicle.views.questions_1', name='questions_1'),
	url(r'^success/$', 'chronicle.views.success', name='success'),
	]
