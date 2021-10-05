from celery import shared_task
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from baz.models import *


@shared_task
def send_baz(**kwargs):
    targets = Target.objects.filter(
        customer__id=kwargs['customer_id']).all()
    bazinga = Baz.objects.filter(pk=kwargs['baz_id']).get()
    subject = bazinga.title
    message = bazinga.content
    email_from = settings.EMAIL_HOST_USER

    customer = Customer.objects.filter(pk=kwargs['customer_id']).get()
    timezone = pytz.timezone(customer.timezone)

    for target in targets:
        try:
            recipient_list = [target.email]
            send_mail(subject, message, email_from, recipient_list)
            status = 1
        except:
            status = 2

        BazHistory.objects.create(
            target=target,
            baz=bazinga,
            status=status,
            sent_at=datetime.now(timezone)
        )
