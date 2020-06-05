import random
import pytz
from django.db import models


def generate():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return "".join(random.choice(chars) for _ in range(12))


class Partner(models.Model):

    id = models.CharField(primary_key=True, editable=False,max_length=200)
    name = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200, blank=True, null=True, choices=[(tz,tz) for tz in pytz.all_timezones])

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        code = self.id
        if not code:
            code = generate()
        while Partner.objects.filter(id=code).exclude(pk=self.pk).exists():
            code = generate()
        self.id = code
        super(Partner, self).save(*args, **kwargs)
