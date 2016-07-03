from django.conf.urls import url, include
from . import views as chronicle_views


urlpatterns = [ 
	url(r'^$', chronicle_views.home, name='home'),
	url(r'^questions/1/$', chronicle_views.questions_1, name='questions_1'),
	url(r'^success/$', chronicle_views.success, name='success'),
	]
