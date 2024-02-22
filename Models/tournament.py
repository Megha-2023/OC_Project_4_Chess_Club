""" Module containing Tournaments class """


class Tournament:
    """
    Class conatining tournaments' details
    """

    def __init__(self, tournament_name: str, tournament_place: str, start_date: str, end_date: str,
                 round_list: list, player_list: list, current_round: str, number_of_rounds: int = 4):
        """
        Constructor
        """
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.tournament_start_date = start_date
        self.tournament_end_date = end_date
        self.round_list = round_list
        self.player_list = player_list
        self.prev_paired_player_list = []
        self.current_round = current_round
        self.number_of_rounds = number_of_rounds

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.tournament_name} + ", " + {self.tournament_place} + ", " + {self.tournament_start_date} \
            + ", " + {self.tournament_end_date}
