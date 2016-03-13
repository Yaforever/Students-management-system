# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.core.urlresolvers import reverse
from stud.models import Group, Student, InfoModels


register = template.Library()

@register.simple_tag
def intoadmin(obj):	
	if obj._meta.db_table == 'stud_group':
		link = reverse('admin:stud_group_change', args=(obj.id,))
	elif obj._meta.db_table == 'stud_student':
		link = reverse('admin:stud_group_change', args=(obj.group.id,))
	elif obj.username:
		link = reverse('admin:auth_user_change', args=(obj.id,))
	else: pass
	return link




