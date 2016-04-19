from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url(r'^$', views.index),
	url(r'^stud/(?P<group_id>[0-9]+)/$', views.students),
	url(r'^edit/$', views.edit, name='edit'),
	url(r'^groupsAPI/$', views.GroupList.as_view()),
	url(r'^groupsAPI/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),
	url(r'^studentsAPI/$', views.StudentList.as_view()),
	url(r'^studentsAPI/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
	
]

urlpatterns = format_suffix_patterns(urlpatterns)