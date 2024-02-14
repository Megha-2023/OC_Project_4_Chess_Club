from datetime import datetime, date
import json
import random
from itertools import combinations
from Models.tournament import Tournament
from Models.round import Round
from Models.match import Match


class TournamentController:
    def __init__(self, view, data, player_controller_obj):
        self.view = view
        self.data = data
        self.tournament = None
        self.player_controller_obj = player_controller_obj
        self.match_dict = {}
        # self.rounds_obj_list: list[Round] = []
        # self.tournament_players_list = []

    def create_tournament(self):
        self.tournament = self.get_tournament_data()
        self.data.add_tournament_to_file(self.tournament)
        
    def get_tournament_data(self):
        user_input = self.view.prompt_for_tournament()
        input_list = user_input.split(", ")
        tournament_name = input_list[0]
        tournament_place = input_list[1]
        tournament_start_date = str(date.today())
        tournament_end_date = ""
        number_of_rounds = input_list[2]
        round_dict = {}
        # create Round
        serialized_round_list = []
        for i in range(int(number_of_rounds)):
            round_dict["round_name"] = "Round" + str(i+1)
            round_dict["match_list"] = []
            round_dict["round_start_date"] = ""
            round_dict["round_end_date"] = ""
            round_obj = self.data.deserialize_round_obj(round_dict)
            # self.rounds_obj_list.append(round_obj)
            serialized_round_list.append(round_obj.__dict__)  # serialize round object into json dict 
            
        player_list = []
        current_round = "0"
        tournament_obj = Tournament(tournament_name, tournament_place, tournament_start_date, tournament_end_date,
                                    serialized_round_list, player_list, current_round, number_of_rounds)
        return tournament_obj
    
    def select_tournament(self):
        all_tournaments = self.data.get_all_tournament_data()
        print("List of existing Tournaments:\n")
        for item in all_tournaments:
            print(f"{item['tournament_name']} at {item['tournament_place']}")
        selected_tournament = self.view.prompt_select_tournament()
        
        return selected_tournament
        
    def add_players_to_tournament(self, tournament_name: str):
        tournament_players_list = []
        tournament_data = self.data.get_selected_tournament(tournament_name)
        self.tournament = self.data.deserialize_tournament(tournament_data)
        
        if len(self.tournament.player_list) < 4:
            print("Tournament must have at least 4 players!")
            answer = "Y"
            while True:
                answer = input("Want to add more players? (Y/N): ")
                if answer == "N" or answer == "n":
                    break
                new_player_obj = self.player_controller_obj.get_player_data()
                self.data.add_player_to_file(new_player_obj)
                player_dict = new_player_obj.__dict__
                tournament_players_list.append(player_dict["national_chess_id"])
        self.data.update_tournament_players(tournament_name, tournament_players_list)
        self.match_dict = self.create_match(tournament_players_list)
        self.update_custom_field_for_round(tournament_name, "match_list", self.match_dict, 1)
        
    def create_match(self, player_list: list):  # to create {"match1": [player,score]} type dict
        match_obj_list = []
        paired_players_dict = self.player_controller_obj.pair_players(player_list)
        
        for key in paired_players_dict.keys():
            player1_dict = self.data.get_player_by_code(paired_players_dict[key][0])
            player1_obj = self.data.deserialize_player_obj(player1_dict)
                        
            player2_dict = self.data.get_player_by_code(paired_players_dict[key][-1])
            player2_obj = self.data.deserialize_player_obj(player2_dict)
            
            match_obj = Match(player1_obj, player2_obj)
            match_obj_list.append(match_obj)
        
        for i in range(len(match_obj_list)):
            self.match_dict["match"+str(i+1)] = (self.data.serialze_match(match_obj_list[i]))
        
        return self.match_dict
    
    def update_custom_field_for_round(self, tournament_name, field_name, field_value, round_number):  # to update speicific field in round_list
        all_rounds_list = self.data.get_rounds_for_tournament(tournament_name)
        original_list = all_rounds_list
        round_name = "Round"+str(round_number)
        
        for i in range(len(original_list)):
            if original_list[i]["round_name"] == round_name:
                key_to_update = i
                current_round_dict = original_list[i]
                current_round_dict[field_name] = field_value
            else:
                continue
        
        original_list[key_to_update] = current_round_dict
        self.data.update_tournament_rounds(tournament_name, original_list, str(round_number))

    def start_round(self, tournament_name: str, round_number: int = 0):
        print(f"Round{round_number} is Started.! Following Matches will be played:\n")
        round_dict = self.data.get_single_round(tournament_name, round_number)
        self.match_dict = round_dict["match_list"]
        for key, value in self.match_dict.items():
            print(f"{key} for Players:{value}")
        self.stop_round(self.match_dict, round_number)

    def stop_round(self, played_match_dict, round_number):
        print(f"======== Round{round_number} is over ===========\n Please Enter Results of the Round")
        player_score_dict = self.update_score(played_match_dict)
        temp_list = self.player_controller_obj.sort_players(player_score_dict)
        i = 1
        for item in temp_list:
            played_match_dict["match"+str(i)] = item
        print(played_match_dict)

    def update_score(self, played_match_dict: dict):
        player_score_dict = {}
        for key, value in played_match_dict.items():
            player_tuple = value
            player_score_dict[player_tuple[0][0]] = player_tuple[0][1]

            player_score_dict[player_tuple[1][0]] = player_tuple[1][1]
        player_score_dict = self.view.ask_for_score(player_score_dict)
        return player_score_dict
    
    
        
    
    

