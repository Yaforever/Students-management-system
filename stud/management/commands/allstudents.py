# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management.base import BaseCommand, CommandError
from stud.models import Student, Group

class Command(BaseCommand):

	def handle(self, *args, **options):
		listof = ''
		groups = Group.objects.all()
		for group in groups:
			listof += '  <<{0}>> :  '.format(group.groupname)
			for st in group.student_set.all():
				listof += '{0}, '.format(st.name)

		self.stdout.write(listof)