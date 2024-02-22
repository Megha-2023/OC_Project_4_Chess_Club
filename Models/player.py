""" Module containing Players class """


class Player:
    """
    Class containing players' details
    """
    def __init__(self, national_chess_id: str, last_name: str, first_name: str, dob: str = ""):
        """
        Constructor
        """
        self.national_chess_id = national_chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.dob = dob

    def __str__(self) -> str:
        """
        Function returns object attributes
        """
        return f"[{self.national_chess_id}]{self.last_name}" + " " + f"{self.first_name}"
