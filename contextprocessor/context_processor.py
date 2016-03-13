from django.conf import settings


def anothercontext(request):
	return {
		'djangosettings': settings
    }