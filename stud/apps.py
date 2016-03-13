from __future__ import unicode_literals
from django.apps import AppConfig


class StudConfig(AppConfig):
	name = 'stud'
	verbose_name = 'Students app'

	def ready(self):
		import stud.signals.handlers