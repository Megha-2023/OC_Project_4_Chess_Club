""" Module containing Players class """


class Player:
    """
    Class containing players' details
    """
    def __init__(self, national_chess_id: str, last_name: str, first_name: str, dob: str = "", score: int = 0):
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
        return f"[{self.national_chess_id}]{self.last_name}" + " " + f"{self.first_name}" + ": " f"{self.score}"

    def get_code(self):
        return self.national_chess_id

    def get_score(self):
        return self.score
