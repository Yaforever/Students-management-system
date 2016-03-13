# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Group, Student, InfoModels
from django.contrib import auth
from django.db import connection


def index(request):
	groups = Group.objects.all()
	student = Student.objects.all()
	user = auth.get_user(request)
	cursor = connection.cursor()
	listgroups = []
	info = InfoModels.objects.order_by('-id')[:10]

	#считаем количество студентов в группах
	for i in groups:
		group_id = i.id
		cursor.execute('SELECT COUNT(*) FROM stud_student WHERE group_id=%s', [group_id])		
		c = cursor.fetchall()
		listgroups.append(c[0][0])
	return render(request, 'stud/index.html', {'groups': groups, 'user': user,
	 'listgroups': listgroups, 'info': info})


def students(request, group_id):
	student = get_object_or_404(Group, pk=group_id)
	username = auth.get_user(request).username
	return render(request, 'stud/student.html', {'student': student, 'username': username})


def edit(request):
	y = range(1970, 2017)
	m = range(1, 13)
	d = range(1, 32)
	groups = Group.objects.all()
	student = Student.objects.all()
	username = auth.get_user(request).username
	cursor = connection.cursor()

	if request.POST:
		#добавить группу
		name = request.POST.get('name', '')
		if name: 
			g = Group(groupname=name)
			g.save()

		#добавить студента
		surname = request.POST.get('surname', '')
		year = request.POST.get('year', '')
		month = request.POST.get('month', '')
		day = request.POST.get('day', '')
		num = request.POST.get('num', '')
		group = request.POST.get('group', '')
		date = '{0}-{1}-{2}'.format(year, month, day)
		if surname and date and num and group: 
			cursor.execute('SELECT id FROM stud_group WHERE groupname=%s', [group])
			groupid = cursor.fetchall()[0][0]
			cursor.execute('INSERT INTO stud_student(group_id, name, date, num) \
				VALUES(%s, %s, %s, %s)', [groupid, surname, date, num])

		#удалить группу
		delgroupid = request.POST.get('delgroup', '')
		if delgroupid: 
			cursor.execute('DELETE FROM stud_student WHERE group_id=%s', [delgroupid])
			cursor.execute('DELETE FROM stud_group WHERE id=%s', [delgroupid])

		#удалить студента
		delstudid = request.POST.get('delstud', '')
		if delstudid: cursor.execute('DELETE FROM stud_student WHERE id=%s', [delstudid])

		#редактировать студента
		rsurname = request.POST.get('rsurname', '')
		ryear = request.POST.get('ryear', '')
		rmonth = request.POST.get('rmonth', '')
		rday = request.POST.get('rday', '')
		rnum = request.POST.get('rnum', '')
		rgroup = request.POST.get('rgroup', '')
		rdate = '{0}-{1}-{2}'.format(ryear, rmonth, rday)
		rstudentid = request.POST.get('rstudid', '')
		if rsurname and rdate and rnum and rgroup: 
			cursor.execute('SELECT id FROM stud_group WHERE groupname=%s', [rgroup])
			groupid = cursor.fetchall()[0][0]
			cursor.execute('UPDATE stud_student SET group_id=%s, name=%s, \
				date=%s, num=%s WHERE id=%s', [groupid, rsurname, rdate, rnum, rstudentid])

		#редактировать группу
		rgroupid = request.POST.get('rgroupid', '')
		rname = request.POST.get('rname', '')
		rmainstudent = request.POST.get('rmainstudent', '')
		if rgroupid:
			cursor.execute('UPDATE stud_group SET groupname=%s, mainstudent=%s WHERE id=%s', 
				[rname, rmainstudent, rgroupid])

		return redirect('/edit/', {'groups': groups, 'student': student, 'username': username, 
			'y': y, 'm': m, 'd': d, 'group': group})
	return render(request, 'stud/edit.html', {'groups': groups, 'student': student, 
		'username': username, 'y': y, 'm': m, 'd': d})

