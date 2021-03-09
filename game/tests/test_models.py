from django.test import TestCase
from game.models import Game

# Testing models

class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Game.objects.create(number_weeks=20, holding_cost=2, backlog_cost=3, player_ids="1,2,3,5",
        info_delay=2, demand_id=2, starting_inventory=40)

    def test_number_weeks_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('number_weeks').verbose_name
        self.assertEqual(field_label, "number weeks")

    def test_has_wholesaler_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('has_wholesaler').verbose_name
        self.assertEqual(field_label, "has wholesaler")
    
    def test_has_retailer_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('has_retailer').verbose_name
        self.assertEqual(field_label, "has retailer")
    
    def test_holding_cost_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('holding_cost').verbose_name
        self.assertEqual(field_label, "holding cost")
    
    def test_backlog_cost_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('backlog_cost').verbose_name
        self.assertEqual(field_label, "backlog cost")

    def test_player_ids_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('player_ids').verbose_name
        self.assertEqual(field_label, "player ids")

    def test_is_game_active_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('is_game_active').verbose_name
        self.assertEqual(field_label, "is game active")
    
    def test_info_sharing_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('info_sharing').verbose_name
        self.assertEqual(field_label, "info sharing")

    def test_info_delay_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('info_delay').verbose_name
        self.assertEqual(field_label, "info delay")

    def test_demand_id_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('demand_id').verbose_name
        self.assertEqual(field_label, "demand id")

    def test_is_default_game_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('is_default_game').verbose_name
        self.assertEqual(field_label, "is default game")
    
    def test_starting_inventory_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('starting_inventory').verbose_name
        self.assertEqual(field_label, "starting inventory")

    def test_player_weeks_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('player_weeks').verbose_name
        self.assertEqual(field_label, "player weeks")
    
    def test_instructor_label(self):
        game = Game.objects.get(game_id=1)
        field_label = game._meta.get_field('instructor').verbose_name
        self.assertEqual(field_label, "instructor")
    
    def test_player_ids_max_length(self):
        game = Game.objects.get(game_id=1)
        max_length = game._meta.get_field('player_ids').max_length
        self.assertEqual(max_length, 20)

    def test_str(self):
        game = Game.objects.get(game_id=1)
        self.assertEqual(game.__str__(), str(game.game_id))

    #i skipped demand id and player weeks max lengths as they should be changed 