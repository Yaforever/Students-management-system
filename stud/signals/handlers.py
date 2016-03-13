from stud.models import Group, Student, InfoModels
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver
from datetime import datetime
import random


@receiver(post_save, sender = Group, dispatch_uid='w')
def signalsave(instance, **kwargs):
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ 'add or change group ' + instance.groupname)
	info.save()

@receiver(post_save, sender = Student, dispatch_uid='w')
def signalsave(instance, **kwargs):
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ 'add or change student ' + instance.name)
	info.save()

@receiver(post_delete, sender = Group, dispatch_uid='w')
def signalsave(instance, **kwargs):
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ 'delete group ' + instance.groupname)
	info.save()

@receiver(post_delete, sender = Student, dispatch_uid='w')
def signalsave(instance, **kwargs):
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ 'delete student ' + instance.name)
	info.save()