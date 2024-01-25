from datetime import date
from Models.tournament import Tournament


class TournamentController:
    def __init__(self, view, data):
        self.view = view
        self.data = data
        self.tournament = None
    
    def create_tournament(self):
        self.tournament = self.get_tournament_data()
        self.data.add_tournament_to_file(self.tournament)

    

    def get_tournament_data(self):
        user_input = self.view.prompt_for_tournament()
        data_list = user_input.split(", ")
        tournament_name =  data_list[0]
        tournament_place = data_list[1]
        tournament_start_date = str(date.today())
        tournament_end_date = ""
        number_of_rounds = data_list[2]

        # create Round
        round_list = []
        i = int(number_of_rounds)
        while i > 0:
            round_input = self.view.prompt_for_round()
            round_list.append(round_input)
            i -= 1
        
        player_list = []
        prev_round = None
        tournament_obj = Tournament(tournament_name, tournament_place, tournament_start_date, tournament_end_date,
                                    round_list, player_list, prev_round, number_of_rounds)
        return tournament_obj