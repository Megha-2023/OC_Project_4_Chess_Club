""" Module containing Players class """
import os
from tinydb import TinyDB, Query

FILENAME = os.path.dirname(os.getcwd()) + "\data\players.json"


class Players:
    """
    Class to register players' details
    """

    def __init__(self, national_chess_id=None, last_name=None, first_name=None, date_of_birth=None):
        self.national_chess_id = national_chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth

    def get_players_data(self, filename: str):

        db = TinyDB(filename)
        print(type(db), db.all())
    
        #with open(filename, 'r', encoding="utf-8") as file:
        #    file_data = file.read()
        #players_data = json.loads(file_data)
        # print(len(db))
        #for key in db:
        #   self.national_chess_id = key[0]['national_chess_id']
        #    self.last_name = key[0]['last_name']
        #    self.first_name = key[0]['first_name']
        #    self.date_of_birth = key[0]['date_of_birth']
        
    def write_players_data(self):
        print(self.national_chess_id)
        print(self.last_name)
        print(self.first_name)


player_obj = Players()
print(FILENAME)
player_obj.get_players_data(FILENAME)
#player_obj.write_players_data()
