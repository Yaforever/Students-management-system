# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User
from forms import LoginForm



def login(request):
	#if attempt to login happened on the page with students, then redirect to the page
	#with students, else redirect to the main page
	if request.session.get('stud'): redir = request.session.get('stud')
	else: redir = '/'

	if request.POST:		
		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#if e-mail in the request, then perform authentication with e-mail 
			if '@' in username:
				email = username
				try:
					u = User.objects.get(email=email)
				except:
					request.session['err'] = 'Incorrect name or password'
					return redirect(redir)
				username = u.username				
			user = auth.authenticate(username=username, password=password)

			if user is not None:
				auth.login(request, user)
				return redirect(redir)
			else:
				request.session['err'] = 'Incorrect name or password'
		else:
			request.session['err'] = 'Incorrect name or password'
			return redirect(redir)
		return redirect(redir)

	else:
		return redirect(redir)
	

def logout(request):
	#if user loged out on the page with students, then redirect to the page
	#with students, else redirect to the main page
	if request.session.get('stud'): redir = request.session.get('stud')
	else: redir = '/'

	auth.logout(request)
	request.session['err'] = ''
	return redirect(redir)

