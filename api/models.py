from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    groups = None
    user_permissions = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=10, blank=True, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Players(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True)
    pic = models.ImageField(blank=True, null=True)

    GENDERS = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS, blank=False)

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

class Team_Owner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Leagues(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=50)
    
class Teams(models.Model):
    name = models.CharField(max_length=20, blank=False)
    team_owner = models.ForeignKey(Team_Owner, on_delete=models.PROTECT)
    league_name = models.ForeignKey(Leagues, on_delete=models.PROTECT)
    goals_for = models.IntegerField(default=0, blank=False)
    goals_against = models.IntegerField(default=0, blank=False)
    score = models.IntegerField(default=0, blank=False)

class TeamPlayerRecords(models.Model):
    player = models.ForeignKey(Players, on_delete=models.PROTECT)
    team = models.ForeignKey(Teams, on_delete=models.PROTECT)
    date_of_joining = models.DateField(auto_now_add=True)
    goals = models.IntegerField(default=0, blank=False)
    number = models.IntegerField(default=0, blank=False, unique=True)

class Campus(models.Model):
    name = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=40, blank=False)

class Field(models.Model):
    name = models.CharField(max_length=20, blank=False)
    campus_name = models.ForeignKey(Campus, on_delete=models.PROTECT)

class Referees(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Match(models.Model):
    team_name1 = models.ForeignKey(Teams, on_delete=models.PROTECT, related_name='team1')
    team_name2 = models.ForeignKey(Teams, on_delete=models.PROTECT, related_name='team2')
    goals_team1 = models.IntegerField(default=0, blank=False)
    goals_team2 = models.IntegerField(default=0, blank=False)
    field_name = models.ForeignKey(Field, on_delete=models.PROTECT)
    referee_name = models.ForeignKey(Referees, on_delete=models.PROTECT)
    date = models.DateField()
