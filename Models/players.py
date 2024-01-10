""" Module containing Players class """


class Players:
    """
    Class containing players' details
    """
    def __init__(self, national_chess_id, last_name, first_name, dob, score=None, rank=None):
        """
        Constructor
        """
        self.national_chess_id = national_chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.dob = dob
        self.score = score
        self.rank = rank

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.last_name} + " " + {self.first_name} + ",[ " + {self.national_chess_id} \
                + "], Score=" + {self.score} + ", Rank=" + {self.rank}
