from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^stud/(?P<group_id>[0-9]+)/$', views.students),
	url(r'^edit/$', views.edit, name='edit'),
	url(r'^addgroup/$', views.addgroup),
	url(r'^addstudent/$', views.addstudent),
	url(r'^deletegroup/(?P<group_id>[0-9]+)/$', views.deletegroup),
	url(r'^redactgroup/(?P<group_id>[0-9]+)/$', views.redactgroup),
	url(r'^deletestudent/(?P<student_id>[0-9]+)/$', views.deletestudent),
	url(r'^redactstudent/(?P<student_id>[0-9]+)/$', views.redactstudent),
]