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
        self.match = ([player_1, player_1.get_score()], [player_2, player_2.score])

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.match[0].first_name} + " = " + {self.match[0].score} + ", " + {self.match[1].first_name} \
                + " = " + {self.match[1].score}
