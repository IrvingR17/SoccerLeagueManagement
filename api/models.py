from django.db import models
from operator import mod
from unicodedata import name
from datetime import datetime, date
import uuid

class Players(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    pic = models.ImageField()

    GENDERS = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS, blank=False)
    phone_number = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=254, blank=False)

    POSITION = (
        ('POR', 'Portero'),
        ('DEF', 'Defensa'),
        ('MED', 'Medio'),
        ('DEL', 'Delantero'),
    )
    position = models.CharField(max_length=3, choices=POSITION, blank=True)

    SANCTION_STATUS = (
        ('D', 'Disponible'),
        ('S', 'Suspendido'),
    )
    sanction_status = models.CharField(max_length=1, choices=SANCTION_STATUS, default="D")

    def __str__(self):
        return self.first_name 

class Team_Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.first_name

class Leagues(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name
    
class Teams(models.Model):
    name = models.CharField(max_length=20, blank=False)
    team_owner_name = models.ForeignKey(Team_Owner, on_delete=models.PROTECT)
    league_name = models.ForeignKey(Leagues, on_delete=models.PROTECT)
    goals_for = models.IntegerField(default=0, blank=False)
    goals_against = models.IntegerField(default=0, blank=False)
    score = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.name 

class TeamPlayerRecords(models.Model):
    player = models.ForeignKey(Players, on_delete=models.PROTECT)
    team = models.ForeignKey(Teams, on_delete=models.PROTECT)
    date_of_joining = models.DateField(auto_now_add=True)
    goals = models.IntegerField(default=0, blank=False)
    number = models.IntegerField(default=0, blank=False, unique=True)

    def __str__(self):
        return "{}_{}".format(self.team.__str__(), self.player.__str__()) 

class Campus(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name

class Field(models.Model):
    name = models.CharField(max_length=20, blank=False)
    campus_name = models.ForeignKey(Campus, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Referees(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.first_name

class Match(models.Model):
    team_name1 = models.ForeignKey(Teams, on_delete=models.PROTECT, related_name='team1')
    team_name2 = models.ForeignKey(Teams, on_delete=models.PROTECT, related_name='team2')
    goals_team1 = models.IntegerField(default=0, blank=False)
    goals_team2 = models.IntegerField(default=0, blank=False)
    field_name = models.ForeignKey(Field, on_delete=models.PROTECT)
    referee_name = models.ForeignKey(Referees, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return "{} vs {}".format(self.team_name1.__str__(), self.team_name2.__str__()) 
