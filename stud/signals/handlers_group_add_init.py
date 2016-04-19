from stud.models import Group, InfoModels
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from datetime import datetime


@receiver(post_init, sender = Group, dispatch_uid='w')
def signalsave(instance, **kwargs):
	info = InfoModels(model_editing=str(datetime.now())[:16] + ' ' 
		+ 'add or change group itit ' + instance.groupname)
	info.save()
