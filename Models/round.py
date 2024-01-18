""" Module containing Rounds class """
from match import Match


class Round:
    """
    Class containing Rounds' details
    """
    def __init__(self, name: str, match_list: list[Match], start_date: str, end_date: str):
        """
        Constructor
        """
        self.round_name = name
        self.match_list = match_list
        self.round_start_date = start_date
        self.round_end_date = end_date

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.round_name} + ", " + {self.matches_list} + ", " + {self.round_start_date} \
                + ", " + {self.round_end_date}
