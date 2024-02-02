"""Module containing Data class to insert/retrieve data to/from json file"""
import os
from tinydb import TinyDB, Query
from Models.player import Player
from Models.tournament import Tournament

FILENAME = os.getcwd() + r"\data\Castle_Chess.json"


class FileData:
    db = TinyDB(FILENAME)
    players_table = db.table('players')
    tournament_table = db.table('tournament')

    def add_player_to_file(self, new_player: Player):
        """ Method to add player's details in json file"""

        data_str = {"national_chess_id": new_player.national_chess_id, "last_name": new_player.last_name,
                    "first_name": new_player.first_name, "DOB": new_player.dob, "score": new_player.score,
                    "rank": new_player.rank}
        
        self.players_table.insert(data_str)
    
    def retrive_all_players_data(self):
        """ Method to get all players' details from json file"""
        
        for item in self.players_table.all():
            print(item)

    def add_tournament_to_file(self, new_tournament: Tournament):
        """ Method to add tournament's details to json file"""

        data_str = {"tournament_name":new_tournament.tournament_name, "tournament_place": new_tournament.tournament_place,
                    "tournament_start_date": new_tournament.tournament_start_date,
                    "tournament_end_date": new_tournament.tournament_end_date,
                    "round_list": new_tournament.round_list, "player_list": new_tournament.player_list,
                    "prev_round": new_tournament.prev_round, "number_of_rounds": new_tournament.number_of_rounds}
        self.tournament_table.insert(data_str)
        print("Tournament details successfully saved to file!!!")
    
    def retrive_all_tournament_data(self):
        """ Method to get all tournaments' details from json file"""

        return self.tournament_table.all()
    
    def retrive_selected_tournament(self, tournament_name: str):
        user_query = Query()
        retrived_data = self.tournament_table.search(user_query.tournament_name == tournament_name)
        return retrived_data
    
    def retrive_selected_players(self, tournament_name: str):
        user_query = Query()
        retrived_data = self.tournament_table.search(user_query.tournament_name == tournament_name)
        return retrived_data[0]['player_list']
    