from baz.models import ScheduleBaz
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=ScheduleBaz)
def schedule_baz(sender, instance, **kwargs):
    print("========")
