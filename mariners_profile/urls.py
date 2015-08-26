from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.data_tables, name='data_tables' ),
	url(r'^profile/$', views.profile, name='profile' ),
]