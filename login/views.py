# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User


def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		if '@' in username:
			email = request.POST.get('username', '')
			try:
				u = User.objects.get(email=email)
			except:
				args['login_error'] = 'Неверный логин или пароль'
				return render(request, 'login/login_.html', args)
			username = u.username				
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = 'Неверный логин или пароль'
			return render(request, 'login/login_.html', args)

	else:
		return render(request, 'login/login_.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')

