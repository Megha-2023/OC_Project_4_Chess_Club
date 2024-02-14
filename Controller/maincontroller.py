import fontstyle

class MainController:
    def __init__(self, view, tournament_contr_obj, data, player_controller_obj):
        self.view = view
        self.tournament_contr_obj = tournament_contr_obj
        self.data = data
        self.player_controller_obj = player_controller_obj
    
    def display_main_menu(self):
        print(fontstyle.apply("!!! Welcome to CASTLE CHESS CLUB !!!", "bold/Italic/BLUE_BG"))
        user_choice = 0
        while user_choice != '0':
            user_choice = self.view.main_menu()
            
            match user_choice:
                case '1':
                    self.display_tournament_menu()
                case '2':
                    self.display_report_menu()
                case _:
                    exit(0)

    def display_tournament_menu(self):
        print("You are now in Tournament Menu \n")
        user_choice = 0
        while user_choice != '0':
            user_choice = self.view.tournament_menu()
            match user_choice:
                case '1':
                    self.tournament_contr_obj.create_tournament()
                case '2':
                    selected_tournament = self.tournament_contr_obj.select_tournament()
                    self.display_tournament_submenu(selected_tournament)
                case _:
                    self.display_main_menu()

    def display_tournament_submenu(self, tournament_name: str):
        submenu_choice = 0
        while submenu_choice != '0':
            selected_players = self.data.get_selected_players(tournament_name)
            if not selected_players or len(selected_players) < 4:
                players_status = False
            else:
                players_status = True
            data_dict = self.data.get_selected_tournament(tournament_name)
            if data_dict["current_round"] == "0":
                round_number = 1
            else:
                round_number = int(data_dict["current_round"])

            submenu_choice = self.view.selected_tournament_submenu(tournament_name, players_status, round_number)
            match submenu_choice:
                case '1':
                    # data_dict = self.data.get_selected_tournament(tournament_name)
                    # data_dict = self.data.serialize_obj(tournament_obj)
                    self.view.display_detailed_list(data_dict)
                case '2':
                    if players_status:
                        print("Players selected for this Tournament:")
                        self.view.display_detailed_list(selected_players)
                    else:
                        self.tournament_contr_obj.add_players_to_tournament(tournament_name)
                case '3':
                    self.tournament_contr_obj.start_round(tournament_name, round_number)
                    
                    # self.tournament_contr_obj.stop_round(tournament_name, played_round, played_match_dict, round_number)
                    
                case '4':
                    show_results(tournament_name)
                case '5':
                    self.data.delete_tournament(tournament_name)
                    print(f"Deleted {tournament_name} Tournament")
                case _:
                    print("Please enter correct choice:")
                    self.display_tournament_menu()
        
    def display_player_menu():
        pass

    def display_report_menu():
        pass

    


    
