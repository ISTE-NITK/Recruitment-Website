from django.conf.urls import url, include
from . import views as create_views


urlpatterns = [ 
	url(r'^$', create_views.home, name='home'),
	url(r'^questions/1/$', create_views.questions_1, name='questions_1'),
	url(r'^success/$', create_views.success, name='success'),
	]
