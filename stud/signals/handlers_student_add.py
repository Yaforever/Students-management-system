from stud.models import Student, InfoModels
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


@receiver(post_save, sender = Student, dispatch_uid='w')
def signalsave(instance, created, **kwargs):
	inf = 'update student'
	if created: inf = 'add student'
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ inf + ' ' + instance.name)
	info.save()
