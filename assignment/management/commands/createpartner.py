import pytz
import random
from datetime import datetime, timedelta, timezone
from faker import Faker
from django.core.management.base import BaseCommand
from assignment.models import Partner, ActivityPeriods

class Command(BaseCommand):
    help = 'Populate data using Faker lib.'

    def _create_partner(self, activity):
        fake = Faker()
        partner = Partner(
            name=fake.name(), 
            timezone=random.choice(pytz.all_timezones),
        )
        partner.save()
        for i in range(activity):
            start = datetime.now(tz=timezone.utc) + timedelta(hours=random.choice(range(1, 12)))
            end = start + timedelta(minutes=random.choice(range(1,60)))
            activity = ActivityPeriods(
                start_datetime=start,
                end_datetime=end,
                partner_id=partner
            )
            activity.save()
    
    # def add_arguments(self, parser):
    #     # Named (optional) arguments
    #     parser.add_argument(
    #         '--delete',
    #         action='delete',
    #         help='Delete partner based on id.',
    #     )

    #     parser.add_argument(
    #         '--create',
    #         action='create',
    #         help='Create partner with name and timezone.',
    #     )

    #     parser.add_argument(
    #         '--read-one',
    #         action='read_one',
    #         help='Read partner based on id',
    #     )

    #     parser.add_argument(
    #         '--read-all',
    #         action='read_all',
    #         help='Read partner based on id',
    #     )

    #     parser.add_argument(
    #         '--update',
    #         action='update',
    #         help='Update partner based on id',
    #     )

    # def delete(self, id=None):
    #     self.stdout.write("delete", ending='')

    # def create(self, id=None):
    #     self.stdout.write("create", ending='')
    
    # def read_one(self, id=None):
    #     self.stdout.write("read one", ending='')
    
    # def read_all(self, id=None):
    #     self.stdout.write("read all", ending='')

    # def update(self, id=None):
    #     self.stdout.write("update", ending='')

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of partner to be created')


    def handle(self, *args, **kwargs):
        for i in range(kwargs['total']):
            self._create_partner(i)