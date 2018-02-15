# Ostmodern Python Code Test

The goal of this exercise is to test that you know your way around Django and
REST APIs. Approach it the way you would an actual long-term project.

The idea is to build a platform on which your users can buy and sell Starships.
To make this process more transparent, it has been decided to source some
technical information about the Starships on sale from the [Starship
API](https://swapi.co/documentation#starships).

A Django project some initial data models have been created already. You may need
to do some additional data modelling to satify the requirements.

## Getting started

* This test works with either
  [Docker](https://docs.docker.com/compose/install/#install-compose) or
  [Vagrant](https://www.vagrantup.com/downloads.html)
* Get the code from `https://github.com/ostmodern/python-code-test`
* Do all your work in your own `develop` branch
* Once you have downloaded the code the following commands will get the site up
  and running

```shell
# For Docker
docker-compose up
# You can run `manage.py` commands using the `./manapy` wrapper

# For Vagrant
vagrant up
vagrant ssh
# Inside the box
./manage.py runserver 0.0.0.0:8008
```
* The default Django "It worked!" page should now be available at
  http://localhost:8008/

## Tasks

Your task is to build a JSON-based REST API for your frontend developers to
consume. You have built a list of user stories with your colleagues, but you get
to decide how to design the API. Remember that the frontend developers will need
some documentation of your API to understand how to use it.

We do not need you to implement users or authentication, to reduce the amount of
time this exercise will take to complete. You may use any external libraries you
require.

* We need to be able to import all existing
  [Starships](https://swapi.co/documentation#starships) to the provided Starship
  Model
* A potential buyer can browse all Starships
* A potential buyer can browse all the listings for a given `starship_class`
* A potential buyer can sort listings by price or time of listing
* To list a Starship as for sale, the user should supply the Starship name and
  list price
* A seller can deactivate and reactivate their listing

After you are done, create a release branch in your repo and send us the link.

## Documentation

#### Getting Started
Run in the order
* `./manage.py migrate`
* `./manage.py ingest_starships`
* `./manage.py runserver 0.0.0.0:8008`

Then go to `localhost:8008/api/starships/`

#### Data Ingest

To ingest Starship data from `https://swapi.co/api/starships/` run the following `manage.py` command:
* `manage.py ingest_starships`

#### Endpoints

 * `/api/forsale/` returns all listing items.
 * `/api/forsale/{id}/` returns the detail view for a listing.
 * `/api/starshops/` returns all Starship classes from the data ingest.

#### Creating a Listing
`/api/forsale/` excepts the `POST` method:

Request:
        
    {
        "name": "Quicksilver",
        "ship_type": {
            "starship_class": "Theta-class T-2c shuttle",
            "manufacturer": "Cygnus Spaceworks",
            "length": 18.5,
            "hyperdrive_rating": 1.0,
            "cargo_capacity": 50000,
            "crew": 5,
            "passengers": 16
        },
        "price": 10
    }
Response = 201 Created

To alter a resources field you can use the `PATCH` method on teh listing ID endpoint, for example:

Request:
`PATCH /api/forsale/6/`

    {
        "price": 200
    }
    
Response = 200 OK:

    {
    "id": 6,
    "name": "zlook",
    "ship_type": {
        "id": 856,
        "starship_class": "H-type Nubian yacht",
        "manufacturer": "Theed Palace Space Vessel Engineering Corps",
        "length": 47.9,
        "hyperdrive_rating": 0.9,
        "cargo_capacity": 0,
        "crew": 4,
        "passengers": 0
    },
    "price": 200,
    "active": true
    }
    
#### How To Deactivate/Activate A Listing
Request:
`PATCH /api/forsale/6/`

    {
            "active": false
    }
    
Response = 200 OK:

    {
    "id": 6,
    "name": "zlook",
    "ship_type": {
        "id": 856,
        "starship_class": "H-type Nubian yacht",
        "manufacturer": "Theed Palace Space Vessel Engineering Corps",
        "length": 47.9,
        "hyperdrive_rating": 0.9,
        "cargo_capacity": 0,
        "crew": 4,
        "passengers": 0
    },
    "price": 200,
    "active": false
    }
    

#### Endpoint Params

The `/api/forsale/` endpoint returns all Starships which have been put up for sale.
It can be ordered by passing the following params:
##### Sorting
* To sort by listing creation date use `/api/forsale/?sort=created`. This returns all items in accending order.
* To sort by price use `/api/forsale/?sort=price`. This returns all items in accending order.
##### Ordering
* To get descending results use the `orderby=` param like this `/api/forsale/?sort=created&orderby=descending`