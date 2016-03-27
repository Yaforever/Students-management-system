# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from models import Group, Student
from django.forms.extras.widgets import SelectDateWidget
import re


def validate_groupname(self):
	if not re.match(r'^([a-zA-Zа-яА-Я0-9]+)([ ]*|[-]?)([a-zA-Zа-яА-Я0-9]+)$', self.strip()):
		raise ValidationError('Please, write only letters and digits, \
			only one hyphenation. Something like "Group-32", "33 MM", "92f5gf9d4f" etc')


def validate_name(self):
	if not re.match(r'^(([a-zA-Zа-яА-Я]+)([ ]*|[-]?)([a-zA-Zа-яА-Я]+))*$', self.strip()):
		raise ValidationError('Please, write only letters and single hyphenations. Something like \
		"Name Surname", "Name Surname-Surname", "Name MiddleName Surname" etc')


class GroupForm(ModelForm):
	
	groupname = forms.CharField(label='Group name', max_length=10, validators=[validate_groupname])

	class Meta:
		model = Group
		fields = ['groupname']
		

class StudentForm(ModelForm):
	
	name = forms.CharField(label='Full name', max_length=30, validators=[validate_name])
	num = forms.IntegerField(min_value=1, max_value=99999)
	group = forms.ModelChoiceField(queryset=Group.objects.all())
	date = forms.DateField(widget=SelectDateWidget(years=(1970, 1971, 1972, 1973,
	 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986,
	  1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
	   2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
	    2012, 2013, 2014, 2015, 2016)))

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



		



			