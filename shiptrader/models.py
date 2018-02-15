from django.db import models


class Starship(models.Model):
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.FloatField(null=True)
    hyperdrive_rating = models.FloatField(null=True)
    cargo_capacity = models.BigIntegerField(null=True)

    crew = models.IntegerField(null=True)
    passengers = models.IntegerField(null=True)

    def __str__(self):
        return self.starship_class


class Listing(models.Model):
    name = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings')
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}-{}-{}".format(self.pk, self.name, self.price)
