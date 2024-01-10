"""Module containing Data class to insert/retrieve data to/from json file"""

import os
from tinydb import TinyDB
from players import Players

FILENAME = os.getcwd() + r"\data\Castle_Chess.json"


class Data:
    db = TinyDB(FILENAME)
    players_table = db.table('players')
    tournament_table = db.table('tournament')

    def add_player_to_file(self, new_player: Players):
        data_str = {"national_chess_id": new_player.national_chess_id, "last_name": new_player.last_name,
                    "first_name": new_player.first_name, "DOB": new_player.dob, "score": new_player.score,
                    "rank": new_player.rank}
        
        self.players_table.insert(data_str)
    

player1 = Players("TS12345", "Disilva", "Anthony", "12/5/1989", 25, 5)
obj = Data()
obj.add_player_to_file(player1)
