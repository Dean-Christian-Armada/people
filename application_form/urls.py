from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.form, name='application_form' ),
	url(r'^tmp-image/$', views.tmp_image, name='tmp_image'),
	url(r'^success/$', views.success, name='success'),
]