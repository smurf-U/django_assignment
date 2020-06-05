from django.db import models
from .partner import Partner


class ActivityPeriods(models.Model):

    start_datetime = models.DateTimeField(help_text="Start time of activity user perform")
    end_datetime = models.DateTimeField(help_text="Start time of activity user perform")
    partner_id = models.ForeignKey(Partner, related_name="activity_periods", on_delete=models.CASCADE, blank=True, null=True)

