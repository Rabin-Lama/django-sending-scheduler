import pytz

from django.db import models


class Customer(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    INTERVAL_IN_WEEKS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ]

    name = models.CharField(max_length=250)
    interval = models.SmallIntegerField(choices=INTERVAL_IN_WEEKS)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    def __str__(self):
        return f'{self.name}'


class Target(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, related_name='employees',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email}'


class Baz(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "bazinga"
        verbose_name_plural = "bazingas"

    def __str__(self):
        return f'{self.title}'


class ScheduleBaz(models.Model):
    customer = models.ForeignKey(Customer, related_name='scheduled_bazingas',
                               on_delete=models.CASCADE)
    baz = models.ForeignKey(Baz, related_name='scheduled_customers',
                            on_delete=models.CASCADE)

    class Meta:
        db_table = 'schedule_baz'
        verbose_name_plural = "Schedule bazingas"

    def __str__(self):
        return f'{self.customer.name} -> {self.baz.title}'


class BazHistory(models.Model):
    SENT_BAZ_STATUSES = [
        (1, 'delivered'),
        (2, 'failed'),
    ]

    target = models.ForeignKey(Target, related_name='baz_history',
                               on_delete=models.CASCADE)
    baz = models.ForeignKey(Baz, related_name='history',
                            on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=SENT_BAZ_STATUSES)
    sent_at = models.DateTimeField()

    class Meta:
        db_table = 'baz_history'
