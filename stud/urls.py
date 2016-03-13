from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^stud/(?P<group_id>[0-9]+)/$', views.students),
	url(r'^edit/$', views.edit, name='edit'),
]