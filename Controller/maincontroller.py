import fontstyle

class MainController:
    def __init__(self, view, tournament, data, player):
        self.view = view
        self.tournament = tournament
        self.data = data
        self.player = player
    
    def display_main_menu(self):
        print(fontstyle.apply("!!! Welcome to CASTLE CHESS CLUB !!!", "bold/Italic/BLUE_BG"))
        user_choice = 0
        while user_choice != '0':
            user_choice = self.view.main_menu()
            
            match user_choice:
                case '1':
                    self.display_player_menu()
                case '2':
                    self.display_tournament_menu()
                case '3':
                    self.display_report_menu()
                case _:
                    exit(0)

    def display_tournament_menu(self):
        print("You are now in Tournament Menu \n")
        user_choice = self.view.tournament_menu()
        match user_choice:
            case '1':
                self.tournament.create_tournament()
            case '2':
                selected_tournament = self.tournament.select_tournament()
                self.display_tournament_submenu(selected_tournament)
            case '3':
                self.tournament.delete_tournament()
            case _:
                self.display_main_menu()

    def display_tournament_submenu(self, tournament_name: str):
        submenu_choice = self.view.selected_tournament_menu(tournament_name)
        match submenu_choice:
            case '1':
                data_list = self.data.retrive_selected_tournament(tournament_name)
                self.view.display_detailed_list(data_list)
            case '2':
                data_list = self.data.retrive_selected_players(tournament_name)
                self.view.display_detailed_list(data_list)
            case '3':
                show_results(tournament_name)
            case '4':
                play_round(tournament_name)
            case _:
                print("Please enter correct choice:")
                self.display_tournament_submenu(tournament_name)
    
    def display_player_menu():
        pass

    def display_report_menu():
        pass

    


    
