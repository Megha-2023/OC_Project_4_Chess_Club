import fontstyle

class MainController:
    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament
    
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
        print(user_choice)
        match user_choice:
            case '1':
                self.tournament.create_tournament()
            case '2':
                self.tournament.update_tournament()
            case '3':
                self.tournament.delete_tournament()
            case _:
                self.display_main_menu()

    def display_player_menu():
        pass

    def display_report_menu():
        pass