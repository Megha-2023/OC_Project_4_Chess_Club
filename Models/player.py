""" Module containing Players class """


class Player:
    """
    Class containing players' details
    """
    def __init__(self, national_chess_id: str, last_name: str, first_name: str, dob: str, score: int = 0):
        """
        Constructor
        """
        self.national_chess_id = national_chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.dob = dob
        self.score = score

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return {self.last_name} + " " + {self.first_name} + ",[ " + {self.national_chess_id} \
                + "], Score=" + {self.score} + ", Rank=" + {self.rank}

    def get_score(self):
        return self.score
