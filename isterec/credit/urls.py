from django.conf.urls import url, include
from . import views as credit_views


urlpatterns = [ 
	url(r'^$', credit_views.home, name='home'),
	url(r'^questions/1/$', credit_views.questions_1, name='questions_1'),
	url(r'^success/$', credit_views.success, name='success'),
	]
