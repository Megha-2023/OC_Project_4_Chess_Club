from datetime import date
from Models.tournament import Tournament
from Controller.playercontroller import PlayerController


class TournamentController:
    def __init__(self, view, data):
        self.view = view
        self.data = data
        self.tournament = None
        self.playercontr_obj = PlayerController(view, data)
    
    def create_tournament(self):
        self.tournament = self.get_tournament_data()
        self.data.add_tournament_to_file(self.tournament)
        if not self.players_list: # check length of list
            print("Enter Players for this tournament")
        else:
            print("Start Matches for the Round")
    

    def get_tournament_data(self):
        user_input = self.view.prompt_for_tournament()
        input_list = user_input.split(", ")
        tournament_name =  input_list[0]
        tournament_place = input_list[1]
        tournament_start_date = str(date.today())
        tournament_end_date = ""
        number_of_rounds = input_list[2]

        # create Round
        round_list = []
        for i in range(number_of_rounds):
            round_input = "Round" + str(i+1)  # no need to ask
            round_list.append(round_input)
        
        player_list = self.players_list
        prev_round = None
        tournament_obj = Tournament(tournament_name, tournament_place, tournament_start_date, tournament_end_date,
                                    round_list, player_list, prev_round, number_of_rounds)
        return tournament_obj
    
    def select_tournament(self):
        all_tournaments = self.data.retrive_all_tournament_data()
        print("List of existing Tournaments:\n")
        for item in all_tournaments:
            print(f"{item['tournament_name']} at {item['tournament_place']}")
        selected_tournament = self.view.prompt_select_tournament()
        
        return selected_tournament
        
    def add_players_to_tournament(self, tournament_name: str):
        if self.tournament.tournament_name == tournament_name:
            if not self.tournament.player_list:
                while len(self.tournament.player_list) < 4:
                    self.tournament.player_list.append(self.playercontr_obj.get_player_data())



        
