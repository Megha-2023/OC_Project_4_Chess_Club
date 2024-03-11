""" Module containing MainController class for navigating through menus"""
import fontstyle


class MainController:
    """ Class contolling all menus' navigations"""

    def __init__(self, view, tournament_contr_obj, data, player_controller_obj, report_contr_obj):
        self.view = view
        self.tournament_contr_obj = tournament_contr_obj
        self.data = data
        self.player_controller_obj = player_controller_obj
        self.report_contr_obj = report_contr_obj

    def display_main_menu(self):
        """ Method to display main menu of the program"""
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
        """ Method to display Tournament related menu"""
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
        """ Method to display menu specific to selected Tournament"""
        submenu_choice = 0
        while submenu_choice != '0':
            selected_players = self.data.get_tournament_players(tournament_name)
            if not selected_players:
                players_status = False
            else:
                players_status = True
            data_dict = self.data.get_selected_tournament(tournament_name)
            number_of_rounds = int(data_dict["number_of_rounds"])
            if int(data_dict["current_round"]) == 0:
                round_number = 1
            else:
                round_number = int(data_dict["current_round"]+1)
            submenu_choice = self.view.selected_tournament_submenu(tournament_name, players_status, round_number, number_of_rounds)
            match submenu_choice:
                case '1':
                    self.view.display_detailed_list(data_dict)
                case '2':
                    if players_status:
                        print("Players selected for this Tournament:")
                        self.report_contr_obj.show_tournament_players(tournament_name)
                    else:
                        self.tournament_contr_obj.disply_associate_player_menu(tournament_name, number_of_rounds)
                case '3':
                    answer = "Y"
                    print(data_dict["current_round"])
                    while round_number <= number_of_rounds:
                        self.tournament_contr_obj.start_round(tournament_name, round_number)
                        answer = input("\n Want to play next round?(Y/N) : ")
                        if answer in ("N", "n"):
                            break
                        round_number += 1
                    if round_number > number_of_rounds:
                        print(fontstyle.apply(f"*** {number_of_rounds} Rounds are played in tournament,"
                                              "\n Tournament is over!", "bold/UNDERLINE"))
                        self.data.update_tournament_end_date(tournament_name)
                case '4':
                    self.tournament_contr_obj.show_results(tournament_name)
                case '5':
                    self.data.delete_tournament(tournament_name)
                    print(fontstyle.apply(f"\nDeleted {tournament_name} Tournament", "bold/UNDERLINE"))
                    self.display_tournament_menu()
                case _:
                    print("Please enter correct choice:")
                    self.display_tournament_menu()

    def display_report_menu(self):
        """ Method to display menu for generating different reports"""
        print("*** Here you can generate the report from the menu\n")
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
                    tournament_name = self.tournament_contr_obj.select_tournament()
                    self.report_contr_obj.show_name_date_tour(tournament_name)
                case '4':
                    tournament_name = self.tournament_contr_obj.select_tournament()
                    self.report_contr_obj.show_tournament_players(tournament_name)
                case '5':
                    tournament_name = self.tournament_contr_obj.select_tournament()
                    self.report_contr_obj.show_rounds_matches(tournament_name)
                case _:
                    self.display_main_menu()
