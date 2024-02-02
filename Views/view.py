import fontstyle


class View:

    def main_menu(self):
        print(fontstyle.apply("*** MAIN MENU ***", "bold/Italic/UNDERLINE/BLUE_BG"))
        choice = input("1 : Player's Menu \n"
                       "2 : Tournament's Menu \n"
                       "3 : Report Menu \n"
                       "0 : Exit \n"
                       "Enter the number of your choice: ")
        return choice
    
    def player_menu(self):
        pass

    def tournament_menu(self):
        print(fontstyle.apply("*** TOURNAMENT MENU ***", "bold/Italic/YELLOW_BG"))
        choice = input("1 : Create New Tournament \n"
                       "2 : Check Existing Tournaments \n"
                       "3 : Delete the Tournament \n"
                       "0 : Return to Main Menu \n"
                       "Enter the number of your choice: ")
        return choice
    
    def selected_tournament_menu(self, tournament_name: str):
        print(fontstyle.apply(f"*** SUBMENU for TOURNAMENT {tournament_name}***", "bold/Italic/YELLOW_BG"))
        choice = input("1 : Show Tournament Details \n"
                       "2 : Show Selected Players \n"
                       "3 : Show Results \n"
                       "4 : Play Next Rounds \n"
                       "Enter the number of your choice: ")
        return choice
    
    def report_menu(self):
        pass

    def prompt_for_tournament(self):
        return input("Enter Tournament details in the given format: [Name, Place, Number_of_Rounds]: ")

    def prompt_select_tournament(self):
        return input("Enter Tournament Name: ")
    
    def prompt_for_player(self):
        return input("Enter Player's details in the given format: [National_Id, LastName, FirstName]: ")
    
    def display_detailed_list(self, data_list: list):
        print(data_list)