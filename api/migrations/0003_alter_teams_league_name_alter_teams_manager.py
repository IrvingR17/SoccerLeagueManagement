# Generated by Django 4.1.1 on 2022-11-11 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_teamplayerrecords_player_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='league_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.leagues'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='manager',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_manager': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]