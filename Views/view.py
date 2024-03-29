""" Module containing view class"""
import fontstyle


class View:
    """ Class to interface with user"""

    def main_menu(self):
        """ Main menu"""
        print(fontstyle.apply("*** MAIN MENU ***", "bold/Italic/UNDERLINE/BLUE_BG"))
        choice = input("1 : Tournament's Menu \n"
                       "2 : Report Menu \n"
                       "0 : Exit \n"
                       "Enter the number of your choice: ")
        return choice

    def tournament_menu(self):
        """ Tournamet menu"""
        print(fontstyle.apply("*** TOURNAMENT MENU ***", "bold/Italic/GREEN_BG"))
        choice = input("1 : Create New Tournament \n"
                       "2 : Check Existing Tournaments \n"
                       "0 : Return to Main Menu \n"
                       "Enter the number of your choice: ")
        return choice

    def report_menu(self):
        """ Report menu"""
        print(fontstyle.apply("\n*** REPORT MENU ***", "bold/Italic/YELLOW_BG"))
        choice = input("1 : Show All Players \n"
                       "2 : Show All Tournaments \n"
                       "3 : Show name and dates of the given Tournament \n"
                       "4 : Show list of players participating in given Tournament \n"
                       "5 : Show All Rounds and Matches of the given Tournament \n"
                       "0 : Return to Main Menu \n"
                       "Enter the number of your choice: ")
        return choice

    def selected_tournament_submenu(self, tournament_name: str, players: bool, round_number: int, total_rounds: int):
        """ Submenu for selected tournament"""
        if players:
            str_player = "2 : Show Selected Players"
        else:
            str_player = "2 : No Players added yet, Add Players for this Tournament"
        if round_number <= total_rounds:
            str_round = "3 : Play Round Number " + str(round_number)
        elif round_number > total_rounds:
            str_round = "3 : Tournament is Over!"
        else:
            str_round = "3 : Play First Round"
        print("\n")
        print(fontstyle.apply(f"*** SUBMENU for TOURNAMENT {tournament_name}***", "bold/Italic/YELLOW_BG"))
        choice = input("1 : Show Tournament Details \n"
                       + str_player + "\n"
                       + str_round + "\n"
                       "4 : Show Results of the Tournament \n"
                       "5 : Delete the Tournament \n"
                       "0 : Return to Tournament Menu \n"
                       "Enter the number of your choice: ")
        return choice

    def prompt_for_tournament(self):
        """ Ask for tournament data"""
        return input("\nEnter Tournament details in the given format: Name, Place, Number_of_Rounds: ")

    def prompt_select_tournament(self):
        """ Ask for tournament"""
        return input("\nEnter Tournament Name: ")

    def prompt_for_player(self):
        """ Ask for new players data"""
        return input("\nEnter Player's details in the given format: National_Id, LastName, FirstName: ")

    def display_detailed_list(self, data_dict):
        """ display given dict"""
        print(data_dict)

    def ask_for_score(self, player_list):
        """ Ask for socre of each player"""
        new_player_list = []
        for i in range(len(player_list)):
            temp_dict = {}
            temp_dict["player_nid"] = player_list[i]["player_nid"]
            temp_dict["score"] = float(input(f"Enter Score for {temp_dict['player_nid']}: "))
            new_player_list.append(temp_dict)
        return new_player_list
