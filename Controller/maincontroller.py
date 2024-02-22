import fontstyle


class MainController:
    def __init__(self, view, tournament_contr_obj, data, player_controller_obj, report_contr_obj):
        self.view = view
        self.tournament_contr_obj = tournament_contr_obj
        self.data = data
        self.player_controller_obj = player_controller_obj
        self.report_contr_obj = report_contr_obj
    
    def display_main_menu(self):
        print(fontstyle.apply("!!! Welcome to CASTLE CHESS CLUB !!!", "bold/Italic/BLUE_BG"))
        main_choice = 0
        while main_choice != '0':
            main_choice = self.view.main_menu()
            
            match main_choice:
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
            selected_players = self.data.get_tournament_players(tournament_name)
            if not selected_players or len(selected_players) < 8:
                players_status = False
            else:
                players_status = True
            data_dict = self.data.get_selected_tournament(tournament_name)
            number_of_rounds = int(data_dict["number_of_rounds"])
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
                        self.tournament_contr_obj.creat_tournament_players(tournament_name)
                case '3':
                    answer = "Y"
                    while round_number <= number_of_rounds:
                        self.tournament_contr_obj.start_round(tournament_name, round_number)
                        # print(f"Round{round_number} is updated Successfull! \n")
                        answer = input(" Want to play next round?(Y/N) : ")
                        if answer == "N" or answer == "n":
                            break
                        round_number += 1
                        
                    if round_number > number_of_rounds:
                        print(f"{number_of_rounds} are played in tournament, \n Tournament is over!")
                        self.data.update_tournament_end_date(tournament_name)
                case '4':
                    show_results(tournament_name)
                case '5':
                    self.data.delete_tournament(tournament_name)
                    print(f"Deleted {tournament_name} Tournament")
                case _:
                    print("Please enter correct choice:")
                    self.display_tournament_menu()
        
    def display_report_menu(self):
        print("!! Here you can generate the report from the menu !! \n")
        report_choice = 0
        while report_choice != '0':
            report_choice = self.view.report_menu()
            print(report_choice)
            match report_choice:
                case '1':
                    self.report_contr_obj.show_all_players()
                case '2':
                    self.report_contr_obj.show_all_tournaments()
                case '3':
                    tournament_name = self.view.prompt_for_tournament()
                    self.report_contr_obj.show_name_date_tour(tournament_name)
                case '4':
                    tournament_name = self.view.prompt_for_tournament()
                    self.report_contr_obj.show_tournament_players(tournament_name)
                case '5':
                    tournament_name = self.view.prompt_for_tournament()
                    self.report_contr_obj.show_rounds_matches(tournament_name)
                case _:
                    self.display_main_menu()
    


    
