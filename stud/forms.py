# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from models import Group, Student
from django.forms.extras.widgets import SelectDateWidget



class GroupForm(ModelForm):
	
	groupname = forms.CharField(label='Group name', max_length=10)

	class Meta:
		model = Group
		fields = ['groupname']
		

class StudentForm(ModelForm):
	years = range(1970, 2030)
	name = forms.CharField(label='Full name', max_length=30)
	num = forms.IntegerField(min_value=1, max_value=99999)
	group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)
	date = forms.DateField(widget=SelectDateWidget(years=years))

	class Meta:
		model = Student
		fields = ['name', 'num', 'group', 'date']


class DelGroup(ModelForm):

	class Meta:
		model = Group
		fields = []
				

class DelStudent(ModelForm):

	class Meta:
		model = Student
		fields = []



		



			