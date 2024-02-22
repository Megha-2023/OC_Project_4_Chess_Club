""" Module containing Matches class """
from Models.player import Player


class Match:
    """
    Class containing Matches' details
    """

    def __init__(self, player_1: Player, score1, player_2: Player, score2):
        """
        Constructor
        """
        self.match = ([player_1.national_chess_id, score1], [player_2.national_chess_id, score2])

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return f"{self.match[0][0].first_name}" + " vs " + f"{self.match[1][0].first_name}"
