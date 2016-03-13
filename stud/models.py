# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver
from datetime import datetime
from django.forms import ModelForm


class Group(models.Model):
	groupname = models.CharField(max_length=10)
	mainstudent = models.CharField(max_length=30, null=True)


class Student(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	date = models.DateField(blank=True)
	num = models.IntegerField(blank=True)


class InfoModels(models.Model):  
	model_editing = models.CharField(max_length=50)

	def __unicode__(self):
		return str(self.model_editing)





