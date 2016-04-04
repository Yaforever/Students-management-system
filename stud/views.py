# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Group, Student, InfoModels
from django.contrib import auth
from forms import GroupForm, StudentForm, DelGroup, DelStudent
from login.forms import LoginForm
from .serializers import GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def group_list(request, format=None):

    if request.method == 'GET':
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def group_detail(request, pk, format=None):

	try:
		groups = Group.objects.get(pk=pk)
	except Group.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = GroupSerializer(groups)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = GroupSerializer(groups, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		groups.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


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


errorsgr = ''
errorsst = ''
errorsrgr = ''
errorsrst = ''

# adding groups
def addgroup(request):
	global errorsgr, errorsst, errorsrgr, errorsrst

	if request.POST:
		request.session["ses"] = False
		#delete old errors
		errorsst = ''
		errorsrgr = ''
		errorsrst = ''
		gform = GroupForm(request.POST)
		
		if gform.is_valid():
			Group.objects.create(groupname=gform.cleaned_data['groupname'])
			errorsgr = ''
		else: 
			errorsgr = gform.errors

	return redirect('/edit/')

#adding students
def addstudent(request):
	global errorsgr, errorsst, errorsrgr, errorsrst

	if request.POST:
		request.session["ses"] = False
		#delete old errors
		errorsgr = ''
		errorsrgr = ''
		errorsrst = ''
		sform = StudentForm(request.POST)
		
		if sform.is_valid():
			Student.objects.create(name=sform.cleaned_data['name'], num=sform.cleaned_data['num'],
					date=sform.cleaned_data['date'], group=sform.cleaned_data['group'])
			errorsst = ''
		else: 
			errorsst = sform.errors

	return redirect('/edit/')

#deleting groups
def deletegroup(request, group_id):
	delgform = DelGroup()	
	Group.objects.filter(id=group_id).delete()
	return redirect('/edit/')

#deleting students
def deletestudent(request, student_id):
	delsform = DelStudent()	
	Student.objects.filter(id=student_id).delete()
	return redirect('/edit/')

#editing groups
def redactgroup(request, group_id):
	global errorsrgr, errorsgr, errorsst, errorsrst

	if request.POST:
		request.session["ses"] = False
		#delete old errors
		errorsgr = ''
		errorsst = ''
		errorsrst = ''
		redgform = GroupForm(request.POST)

		if redgform.is_valid():
			Group.objects.filter(id=group_id).update(groupname=redgform.cleaned_data['groupname'], 
				mainstudent=request.POST.get('mainstudent', 'Unknown'))
			errorsrgr = ''
		else:
			errorsrgr = redgform.errors

	return redirect('/edit/')

#editing students
def redactstudent(request, student_id):
	global errorsrgr, errorsrst, errorsgr, errorsst

	if request.POST:
		request.session["ses"] = False
		#delete old errors
		errorsgr = ''
		errorsst = ''
		errorsrgr = ''
		redsform = StudentForm(request.POST)

		if redsform.is_valid():
			Student.objects.filter(id=student_id).update(name=redsform.cleaned_data['name'], 
				num=redsform.cleaned_data['num'], date=redsform.cleaned_data['date'], 
				group=redsform.cleaned_data['group'])
			errorsrgr = ''
		else:
			errorsrgr = redsform.errors

	return redirect('/edit/')


def edit(request):
	global errorsgr, errorsst, errorsrgr, errorsrst

	groups = Group.objects.all()
	student = Student.objects.all()
	username = auth.get_user(request).username
	gform = GroupForm()
	sform = StudentForm()
	redgform = GroupForm()
	redsform = StudentForm()
	#if the edit page had refreshed, then delete all errors
	if request.session.get('ses') == True:
		errorsgr = ''
		errorsst = ''
		errorsrgr = ''
	request.session["ses"] = True

	return render(request, 'stud/edit.html', {'groups': groups, 'student': student, 
		'username': username, 'gform': gform, 'sform': sform, 'redgform': redgform, 
		'redsform': redsform, 'errorsgr': errorsgr, 'errorsst': errorsst, 
		'errorsrgr': errorsrgr, 'errorsrst': errorsrst})




