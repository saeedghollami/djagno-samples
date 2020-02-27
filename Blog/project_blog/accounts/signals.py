from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Profile


# singal = event
# reciver = event handler

def save_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


post_save.connect(save_profile, sender=User)