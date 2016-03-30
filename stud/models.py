# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.forms import ModelForm


class InfoModels(models.Model):  
	model_editing = models.CharField(max_length=50)

	def __unicode__(self):
		return str(self.model_editing)


class Group(models.Model):
	groupname = models.CharField(max_length=10)
	mainstudent = models.CharField(max_length=30, default='Unknown')

	def __unicode__(self):
		return self.groupname


class Student(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	date = models.DateField(blank=True)
	num = models.IntegerField(blank=True)

	def __unicode__(self):
		return self.name








