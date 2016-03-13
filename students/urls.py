from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	url(r'^', include('stud.urls', )),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^auth/', include('login.urls')),
]
