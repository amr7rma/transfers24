from django.db import models
from django.db.models import *
from django.forms import CharField


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    max_income = models.FloatField(blank=True, null=True)
    max_expend = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.FloatField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    old_club = models.ForeignKey(Club, on_delete=CASCADE, related_name='old_club')
    new_club = models.ForeignKey(Club, on_delete=CASCADE, related_name='new_club')
    price = models.FloatField()
    price_tft = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.player
