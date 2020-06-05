from django.contrib import admin
from .models import Partner, ActivityPeriods


class ActivityPeriodsAdminInline(admin.TabularInline):
    model = ActivityPeriods

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    inlines = (ActivityPeriodsAdminInline, )



