# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Group, Student


class StudentInline(admin.StackedInline):
	model = Student
	extra = 4

class GroupAdmin(admin.ModelAdmin):
    fields = ['groupname', 'mainstudent']
    inlines = [StudentInline]
    
    list_display = ('groupname',)

admin.site.register(Group, GroupAdmin)
