from django.core.management.base import BaseCommand
from shiptrader.utlis import starship_data_ingest


class Command(BaseCommand):

    help = 'Ingest latest Starship data'

    def handle(self, *args, **options):
        starship_data_ingest()


