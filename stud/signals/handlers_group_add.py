from stud.models import Group, InfoModels
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from datetime import datetime


@receiver(post_save, sender = Group, dispatch_uid='w')
def signalsave(instance, created, **kwargs):
	inf = 'update group'
	if created: inf = 'add group'
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ inf + ' ' + instance.groupname)
	info.save()
