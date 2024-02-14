import fontstyle


class View:

    def main_menu(self):
        print(fontstyle.apply("*** MAIN MENU ***", "bold/Italic/UNDERLINE/BLUE_BG"))
        choice = input("1 : Tournament's Menu \n"
                       "2 : Report Menu \n"
                       "0 : Exit \n"
                       "Enter the number of your choice: ")
        return choice
    
    def player_menu(self):
        pass

    def tournament_menu(self):
        print(fontstyle.apply("*** TOURNAMENT MENU ***", "bold/Italic/YELLOW_BG"))
        choice = input("1 : Create New Tournament \n"
                       "2 : Check Existing Tournaments \n"
                       "0 : Return to Main Menu \n"
                       "Enter the number of your choice: ")
        return choice
    
    def selected_tournament_submenu(self, tournament_name: str, players: bool, round_number: int):
        if players:
            str_player = "2 : Show Selected Players"
        else:
            str_player = "2 : No Players selected yet, Add Players for this Tournament"
        if round_number != 1:
            str_round = "3 : Play Next Round"
        else:
            str_round = "3 : Start First Round"
        print(fontstyle.apply(f"*** SUBMENU for TOURNAMENT {tournament_name}***", "bold/Italic/YELLOW_BG"))
        choice = input("1 : Show Tournament Details \n"
                       + str_player + "\n"
                       + str_round+ "\n"
                       "4 : Show Results of Tournament \n"
                       "5 : Delete the Tournament \n"
                       "0 : Return to Tournament Menu \n"
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
    
    def display_detailed_list(self, data_dict):
        print(data_dict)

    def ask_for_score(self, sort_dic: dict):
        for key in sort_dic.keys():
            score = input(f"Enter socre of {key}: ")
            sort_dic[key] = score
        return sort_dic
