from __future__ import unicode_literals
from django.apps import AppConfig


class StudConfig(AppConfig):
	name = 'stud'
	verbose_name = 'Students app'

	def ready(self):
		import stud.signals.handlers_student_delete, stud.signals.handlers_group_add, stud.signals.handlers_group_delete, stud.signals.handlers_student_add