from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Game(models.Model):
    game_id = models.AutoField(primary_key=True) ##
    session_length = models.IntegerField(default=24)
    number_weeks = models.IntegerField()
    has_distributor = models.BooleanField(default=True)
    has_wholesaler = models.BooleanField(default=True)
    holding_cost = models.IntegerField()
    backlog_cost = models.IntegerField()
    
    #player_ids = ArrayField(models.IntegerField(), blank=True)
    player_ids = models.CharField(max_length=20)
    is_game_active = models.BooleanField(default=True)
    info_sharing = models.BooleanField(default=True)
    info_delay = models.IntegerField()
    demand_id = models.CharField(max_length=5)
    is_default_game = models.BooleanField(default=True)
    starting_inventory = models.IntegerField()
    #player_weeks = ArrayField(models.IntegerField(), blank=True)
    player_weeks = models.CharField(max_length=20, blank=True)
    
    #function should always return string 
    def __str__(self):
	    return str(self.game_id)