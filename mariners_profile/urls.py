from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='data_tables' ),
	url(r'^(?P<id>[0-9]*)/$', views.profile, name='profile' ),
]