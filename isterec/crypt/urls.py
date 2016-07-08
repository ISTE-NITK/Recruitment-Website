from django.conf.urls import url, include
from . import views as crypt_views


urlpatterns = [ 
	url(r'^$', crypt_views.home, name='home'),
	url(r'^questions/1/$', crypt_views.questions_1, name='questions_1'),
	url(r'^upload/$', crypt_views.upload, name='upload'),
	url(r'^success/$', crypt_views.success, name='success'),]
