# Generated by Django 4.1.1 on 2022-09-30 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('campus_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.campus')),
            ],
        ),
        migrations.CreateModel(
            name='Leagues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='')),
                ('gender', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('position', models.CharField(blank=True, choices=[('POR', 'Portero'), ('DEF', 'Defensa'), ('MED', 'Medio'), ('DEL', 'Delantero')], max_length=3)),
                ('sanction_status', models.CharField(choices=[('D', 'Disponible'), ('S', 'Suspendido')], default='D', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('goals_for', models.IntegerField(default=0)),
                ('goals_against', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('league_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.leagues')),
                ('team_owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.team_owner')),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayerRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_joining', models.DateField(auto_now_add=True)),
                ('goals', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0, unique=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.players')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.teams')),
            ],
        ),
        migrations.CreateModel(
            name='Referees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team1', models.IntegerField(default=0)),
                ('goals_team2', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('field_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.field')),
                ('referee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.referees')),
                ('team_name1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team1', to='api.teams')),
                ('team_name2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team2', to='api.teams')),
            ],
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
