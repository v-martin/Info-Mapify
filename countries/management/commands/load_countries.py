import csv
from django.core.management import BaseCommand
from loguru import logger
from countries.models import Country


class Command(BaseCommand):
    """An instance of runnable `manage.py` command."""

    def handle(self, filename: str, *args, **options) -> None:
        """This method parses input data and converts it to :model:`countries.Country` entities.

        :param filename: The name of the input file that is parsed.
        :type filename: str

        :return: None
        """
        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                country, is_created = Country.objects.get_or_create(
                    name=row[0]
                )
                if is_created:
                    logger.debug(f'Country {country.name} created!')
                else:
                    logger.debug(f'Country {country.name} already exists!')
