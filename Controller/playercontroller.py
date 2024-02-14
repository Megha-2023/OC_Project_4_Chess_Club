import random
from Models.player import Player
from Models.match import Match


class PlayerController:
    def __init__(self, view, data):
        self.view = view
        self.data = data
        self.player = None
    
    def get_player_data(self):
        user_input = self.view.prompt_for_player()
        input_list = user_input.split(", ")
        national_chess_id = input_list[0]
        last_name = input_list[1]
        first_name = input_list[2]
        
        player_obj = Player(national_chess_id, last_name, first_name)
        return player_obj

    def sort_players(self, player_score_dict: dict):
        return sorted(player_score_dict.items(), key=lambda kv: (kv[1], kv[0]))
    
    def pair_players(self, player_list):
        pairs = {}
        for p in range(0, len(player_list), 2):
            pairs[p+1] = (player_list[p], player_list[p+1])
            p += 1
        return pairs
    