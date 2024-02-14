""" Module containing Matches class """
from Models.player import Player


class Match:
    """
    Class containing Matches' details
    """

    def __init__(self, player_1: Player, player_2: Player):
        """
        Constructor
        """
        self.match = ([player_1.get_code(), player_1.get_score()], [player_2.get_code(), player_2.get_score()])

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return f"{self.match[0][0].first_name}" + " vs " +  f"{self.match[1][0].first_name}"
    

