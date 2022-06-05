from ast import Mod
from random import choices
from secrets import choice
from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    country=models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countries')
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='staties')
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class PopulationModule(models.Model):
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O', 'Other')
    )
    Group_CHOICES=(
    ('old','Old'),
    ('young','Young'),
    ('child', 'Child')
    )
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='populations')
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    age_group=models.CharField(max_length=10, choices=Group_CHOICES)
    population=models.PositiveIntegerField()

    def __str__(self):
        return self.city.name
