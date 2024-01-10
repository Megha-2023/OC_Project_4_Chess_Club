""" Module containing Rounds class """


class Rounds:
    """
    Class containing Rounds' details
    """
    def __init__(self, name, matches_list, start_date, end_date):
        """
        Constructor
        """
        self.round_name = name
        self.matches_list = matches_list
        self.round_start_date = start_date
        self.round_end_date = end_date

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.round_name} + ", " + {self.matches_list} + ", " + {self.round_start_date} \
                + ", " + {self.round_end_date}
