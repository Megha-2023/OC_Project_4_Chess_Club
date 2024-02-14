"""Module containing Data class to insert/retrieve data to/from json file"""
import os
import json
from types import SimpleNamespace as Namespace
from tinydb import TinyDB, Query, where
from Models.player import Player
from Models.round import Round
from Models.tournament import Tournament
from Models.match import Match

FILENAME = os.getcwd() + r"\data\Castle_Chess.json"


class FileData:
    db = TinyDB(FILENAME)
    players_table = db.table('players')
    tournament_table = db.table('tournament')

    def add_player_to_file(self, new_player: Player):
        """ Method to add player's details in json file"""

        data_str = {"national_chess_id": new_player.national_chess_id, "last_name": new_player.last_name,
                    "first_name": new_player.first_name, "DOB": new_player.dob, "score": new_player.score}
        
        self.players_table.insert(data_str)
    
    def get_all_players_data(self):
        """ Method to get all players' details from json file"""
        
        return self.players_table.all()

    def add_tournament_to_file(self, new_tournament: Tournament):
        """ Method to add tournament's details to json file

       data_str = {"tournament_name":new_tournament.tournament_name, "tournament_place": new_tournament.tournament_place,
                    "tournament_start_date": new_tournament.tournament_start_date,
                    "tournament_end_date": new_tournament.tournament_end_date,
                    "round_list": new_tournament.round_list, "player_list": new_tournament.player_list,
                    "current_round": new_tournament.current_round, "number_of_rounds": new_tournament.number_of_rounds}
        """
        data_dict = new_tournament.__dict__
        # data_str = self.serialize_obj(new_tournament)
        self.tournament_table.insert(data_dict)
        print("Tournament details successfully saved to file!!!")
    
    def get_all_tournament_data(self):
        """ Method to get all tournaments' details from json file"""

        return self.tournament_table.all()
    
    def get_selected_tournament(self, tournament_name: str):
        user_query = Query()
        retrived_data = self.tournament_table.search(user_query.tournament_name == tournament_name)
        return retrived_data[0]
        
    def get_player_by_code(self, national_chess_id: str):
        user_query = Query()
        retrived_data = self.players_table.search(user_query.national_chess_id == national_chess_id)
        return retrived_data[0]
    
    def deserialize_tournament(self, tournament_dict: dict):
        tournament_obj = Tournament(tournament_dict["tournament_name"], tournament_dict["tournament_place"],
                                    tournament_dict["tournament_start_date"], tournament_dict["tournament_end_date"],
                                    tournament_dict["round_list"], tournament_dict["player_list"],
                                    tournament_dict["current_round"], tournament_dict["number_of_rounds"])
        return tournament_obj

    def update_tournament_players(self, tournament_name: str, player_list: list):
        user_query = Query()
        self.tournament_table.update({"player_list": player_list}, user_query["tournament_name"] == f"{tournament_name}")

    def update_tournament_rounds(self, tournament_name: str, round_list: list, current_round: str):
        user_query = Query()
        self.tournament_table.update({"round_list": round_list, "current_round": current_round}, user_query["tournament_name"] == f"{tournament_name}")

    def get_selected_players(self, tournament_name: str):
        user_query = Query()
        retrived_data = self.tournament_table.search(user_query.tournament_name == tournament_name)
        return retrived_data[0]['player_list']
    
    def get_rounds_for_tournament(self, tournament_name: str):  # get all rounds in list
        user_query = Query()
        retrived_data = self.tournament_table.search(user_query.tournament_name == tournament_name)
        all_rounds_list = retrived_data[0]['round_list']
        return all_rounds_list
    
    def get_single_round(self, tournament_name: str, round_number):  # get dict of single round
        user_query = Query()
        retrived_data = self.tournament_table.get((user_query.tournament_name == tournament_name))
        single_round_dict = retrived_data["round_list"][round_number-1]
        return single_round_dict
       
    def delete_tournament(self, tournament_name: str):
        self.tournament_table.remove(where("tournament_name") == tournament_name)

    def serialize_round_obj(self, round_obj: Round):
        round_dict = json.dumps(round_obj.__dict__())
        # round_dict = {"round_name": round_obj.round_name, "match_list": round_obj.match_list,
        #              "round_start_date": round_obj.round_start_date, "round_end_date": round_obj.round_end_date}
        return round_dict
    
    def deserialize_round_obj(self, round_dict: dict):
        round_obj = Round(round_dict["round_name"], round_dict["match_list"],
                          round_dict["round_start_date"], round_dict["round_end_date"])
        return round_obj
    
    def serialize_player_obj(self, player_obj: Player):
        player_dict = {"national_chess_id": player_obj.national_chess_id, "last_name": player_obj.last_name,
                       "first_name": player_obj.first_name, "dob": player_obj.dob}
        return player_dict
    
    def deserialize_player_obj(self, player_dict: dict):
        player_obj = Player(player_dict["national_chess_id"], player_dict["last_name"],
                            player_dict["first_name"])
        return player_obj
    
    def serialize_obj(self, object):
        data_dict = json.dumps(object.__dict__)
        return data_dict
    
    def serialze_match(self, match_obj: Match):
        match_dict = match_obj.__dict__
        return match_dict['match']
    
    def update_score(self, tournament_name: str, played_match_dict: dict, round_number: int):
        pass