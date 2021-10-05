import json
import datetime

from .models import *
from django.contrib import admin
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(Baz)
class BazAdmin(admin.ModelAdmin):
    pass


@admin.register(ScheduleBaz)
class ScheduleBazAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        instance = form.instance
        instance.save()

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=obj.customer.interval * 5,
            # every=obj.customer.interval * 7 * 86400,
            period=IntervalSchedule.SECONDS,
        )

        today = datetime.date.today()
        tuesday = today + datetime.timedelta((1 - today.weekday()) % 7)

        PeriodicTask.objects.create(
            interval=schedule,
            name=f'Send {obj.baz.title} to {obj.customer.name} employees',
            task='baz.tasks.send_baz',
            kwargs=json.dumps(
                {"customer_id": obj.customer.id, "baz_id": obj.baz.id}),
            start_time=tuesday
        )
