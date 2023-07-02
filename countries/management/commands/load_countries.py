import csv
from django.core.management import BaseCommand
from loguru import logger
from countries.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('test.txt') as f:
            reader = csv.reader(f)
            for row in reader:
                country, is_created = Country.objects.get_or_create(
                    name=row[0]
                )
                if is_created:
                    logger.debug(f'Country {country.name} created!')
                else:
                    logger.debug(f'Country {country.name} already exists!')


