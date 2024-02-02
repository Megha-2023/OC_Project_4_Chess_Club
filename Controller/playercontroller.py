from Models.player import Player


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
        dob = None
        
        player_obj = Player(national_chess_id, last_name, first_name, dob)
        return player_obj
