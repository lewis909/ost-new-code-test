import requests

from testsite.settings import STARSHIP_API_URL
from shiptrader.models import Starship


def starship_data_ingest():
    url = STARSHIP_API_URL

    response = requests.get(url)
    next_page = response.json()['next']

    while next_page is not None:

        starships = response.json()['results']
        next_page = response.json()['next']

        for ship in starships:

            if ship['hyperdrive_rating'] == 'unknown':
                ship['hyperdrive_rating'] = 0.0
            if ship['crew'] == 'unknown':
                ship['crew'] = 0
            if ship['passengers'] == 'unknown':
                ship['passengers'] = 0
            if ship['length'] == 'unknown':
                ship['length'] = 0
            if ship['cargo_capacity'] == 'unknown':
                ship['cargo_capacity'] = 0

            if type(ship['hyperdrive_rating']) == str:
                ship['hyperdrive_rating'] = ship[
                    'hyperdrive_rating'].replace(',', '.')
            if type(ship['cargo_capacity']) == str:
                ship['cargo_capacity'] = ship[
                    'cargo_capacity'].replace(',', '')
            if type(ship['crew']) == str:
                ship['crew'] = ship[
                    'crew'].replace(',', '')
            if type(ship['passengers']) == str:
                ship['passengers'] = ship[
                    'passengers'].replace(',', '')
            if type(ship['length']) == str:
                ship['length'] = ship[
                    'length'].replace(',', '')

            # Check Starship is not already ingested
            starship = Starship.objects.filter(
                starship_class=ship['model'],
                manufacturer=ship['manufacturer']
            )

            if starship:
                continue

            Starship.objects.create(
                starship_class=ship['model'],
                manufacturer=ship['manufacturer'],
                length=ship['length'],
                hyperdrive_rating=float(ship['hyperdrive_rating']),
                cargo_capacity=int(ship['cargo_capacity']),
                crew=int(ship['crew']),
                passengers=int(ship['passengers'])

            )
        if not next_page:
            break
        response = requests.get(next_page)

    print(len(Starship.objects.all().values()))