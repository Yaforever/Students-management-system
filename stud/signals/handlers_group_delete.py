from stud.models import Group, InfoModels
from django.db.models.signals import post_delete
from django.dispatch import receiver
from datetime import datetime


@receiver(post_delete, sender = Group, dispatch_uid='w')
def signalsave(instance, **kwargs):
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ 'delete group ' + instance.groupname)
	info.save()

