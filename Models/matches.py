""" Module containing Matches class """


class Matches:
    """
    Class containing Matches' details
    """

    def __init__(self, player_1, player_2):
        """
        Constructor
        """
        self.match = (player_1, player_2)

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.match[0].first_name} + " = " + {self.match[0].score} + ", " + {self.match[1].first_name} \
                + " = " + {self.match[1].score}
