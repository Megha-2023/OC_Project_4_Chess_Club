""" Module containing PlayerController class to interact between view and Player class"""
import random
from Models.player import Player


class PlayerController:
    """ Class controlling Players' related operations"""

    def __init__(self, view, data):
        self.view = view
        self.data = data
        self.player = None

    def get_player_data(self):
        """ Method to ask for new player data"""
        try:
            user_input = self.view.prompt_for_player()
            input_list = user_input.split(", ")
            national_chess_id = input_list[0]
            last_name = input_list[1]
            first_name = input_list[2]
        except IndexError:
            print("Please Enter data in given format")

        player_obj = Player(national_chess_id, last_name, first_name)
        return player_obj

    def sort_players(self, updated_player_score_list):
        """ Method to sort player and score dict by score in descending order"""
        updated_player_score_list.sort(key=lambda x: x['score'], reverse=True)
        return updated_player_score_list

    def pair_players(self, player_list, prev_paired_list):
        """ Method to Pair players not repeating previously paired players"""
        new_paired_list = []
        new_score_list = []

        for i in range(0, len(player_list), 2):
            player1 = player_list[i]
            player2 = player_list[i + 1] if i + 1 < len(player_list) else None

            if player2:
                # Check if players have played against each other before
                if (player1["player_nid"], player2["player_nid"]) in prev_paired_list:
                    # Find another player to pair with player1
                    for j in range(i + 2, len(player_list)):
                        if (player1["player_nid"], player_list[j]["player_nid"]) not in prev_paired_list:
                            player2 = player_list[j]
                            break

                new_paired_list.append((player1["player_nid"], player2["player_nid"]))
                new_score_list.append((player1["score"], player2["score"]))
        return new_paired_list, new_score_list

    def merge_list_to_dict(self, player_tuple_list, score_tuple_list):
        """ Method to merge 2 different list in one single dict containing player_nid and score"""
        temp_list = []
        for k, item in enumerate(player_tuple_list):  #range(0, len(player_tuple_list)):
            for j in [0, 1]:
                temp_dict = {}
                temp_dict["player_nid"] = player_tuple_list[k][j]
                temp_dict["score"] = score_tuple_list[k][j]
                temp_list.append(temp_dict)
        return temp_list

    def random_pair(self, player_list):
        """ Method to pair players randomly"""
        total = len(player_list)
        paired_list = []
        for i in range(0, total):
            random_index = random.randrange(0, len(player_list))
            pl1 = player_list.pop(random_index)
            paired_list.append(pl1)
            total -= 1
        return paired_list
