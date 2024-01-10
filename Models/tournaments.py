""" Module containing Tournaments class """


class Tournaments:
    """
    Class conatining tournaments' details
    """

    def __init__(self, tournament_name, tournament_place, start_date, end_date,
                 rounds_list, players_list, details, number_of_rounds=4):
        """
        Constructor
        """
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.tournament_start_date = start_date
        self.tournament_end_date = end_date
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = details
        self.number_of_rounds = number_of_rounds

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.tournament_name} + ", " + {self.tournament_place} + ", " + {self.tournament_start_date} \
            + ", " + {self.tournament_end_date}
