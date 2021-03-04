from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Game(models.Model):
    game_id = models.AutoField(primary_key=True) ##
    session_length = models.IntegerField(default=24)
    number_weeks = models.IntegerField()
    has_distributor = models.BooleanField(default=False)
    has_wholesaler = models.BooleanField(default=False)
    holding_cost = models.IntegerField()
    backlog_cost = models.IntegerField()
    player_ids = ArrayField(models.IntegerField(), blank=True)
    is_game_active = models.BooleanField(default=True)
    info_sharing = models.BooleanField(default=True)
    info_delay = models.IntegerField()
    demand_id = models.CharField(max_length=5)
    is_default_game = models.BooleanField(default=True)
    starting_inventory = models.IntegerField()
    player_weeks = ArrayField(models.IntegerField(), blank=True)
    
    def __str__(self):
	    return self.game_id