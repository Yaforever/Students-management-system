# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Group, Student, InfoModels
from django.contrib import auth
from forms import GroupForm, StudentForm, DelGroup, DelStudent
from login.forms import LoginForm
from .serializers import GroupSerializer, StudentSerializer
from rest_framework import generics
from django.http import HttpResponse


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def index(request):
	groups = Group.objects.all()
	student = Student.objects.all()
	user = auth.get_user(request)
	listgroups = []
	info = InfoModels.objects.order_by('-id')[:10]
	form = LoginForm()
	err = request.session.get('err')
	request.session['stud'] = ''
	#if the main page had refreshed, then delete all errors
	if request.session.get("ses") == True:
		request.session['err'] = ''	

	request.session["ses"] = True
	#counting amount of students in the each group
	for i in groups: 
		c = Student.objects.filter(group_id=i.id).count()
		listgroups.append(c)
	return render(request, 'stud/index.html', {'groups': groups, 'user': user,
	 'listgroups': listgroups, 'info': info, 'form': form, 'err': err})


def students(request, group_id):
	student = get_object_or_404(Group, pk=group_id)
	form = LoginForm()
	err = request.session.get('err')
	request.session['stud'] = '/stud/{0}/'.format(group_id)
	username = auth.get_user(request).username
	#if the page with student had refreshed, then delete all errors
	if request.session.get("ses") == True:
		request.session['err'] = ''

	request.session["ses"] = True
	return render(request, 'stud/student.html', {'student': student, 
		'username': username, 'form': form, 'err': err})


def edit(request):

	groups = Group.objects.all()
	student = Student.objects.all()
	username = auth.get_user(request).username
	gform = GroupForm()
	sform = StudentForm()
	redgform = GroupForm()
	redsform = StudentForm()
	form = LoginForm()
	err = request.session.get('err')
	request.session['stud'] = '/edit/'
	#if the main page had refreshed, then delete all errors
	if request.session.get("ses") == True:
		request.session['err'] = ''	

	request.session["ses"] = True

	return render(request, 'stud/edit.html', {'groups': groups, 'student': student, 
		'username': username, 'gform': gform, 'sform': sform, 'redgform': redgform, 
		'redsform': redsform, 'form': form, 'err': err})




