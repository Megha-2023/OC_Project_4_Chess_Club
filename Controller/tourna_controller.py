from datetime import datetime, date
import fontstyle
from Models.tournament import Tournament
from Models.match import Match


class TournamentController:
    def __init__(self, view, data, player_controller_obj):
        self.view = view
        self.data = data
        self.tournament = None
        self.player_controller_obj = player_controller_obj
        self.round_list = []
        self.tournament_players_list = []
        self.previous_paired_players_list = []

    def create_tournament(self):
        self.tournament = self.get_tournament_data()
        self.data.add_tournament_to_file(self.tournament)

    def get_tournament_data(self):
        try:
            user_input = self.view.prompt_for_tournament()
            input_list = user_input.split(", ")
            tournament_name = input_list[0]
            tournament_place = input_list[1]
            tournament_start_date = str(date.today())
            tournament_end_date = ""
            if input_list[2]:
                number_of_rounds = input_list[2]
            else:
                number_of_rounds = 4
        except IndexError:
            print("Please Enter data in given format")

        self.round_list = []

        if not self.tournament_players_list:
            print(f"No Players Selected for Tournament {tournament_name}.\n Enter Players")
            self.tournament_players_list = self.creat_tournament_players(tournament_name, number_of_rounds)

        self.prev_paired_player_list = []
        current_round = "0"
        tournament_obj = Tournament(tournament_name, tournament_place, tournament_start_date, tournament_end_date,
                                    self.round_list, self.tournament_players_list, current_round, number_of_rounds)
        return tournament_obj

    def select_tournament(self):
        all_tournaments = self.data.get_all_tournament_data()
        print(fontstyle.apply("\nList of existing Tournaments:\n", "bold/UNDERLINE"))
        print(fontstyle.apply("NAME\tPLACE", "bold/UNDERLINE"))
        for item in all_tournaments:
            print(f"{item['tournament_name']}\t{item['tournament_place']}")
        selected_tournament = self.view.prompt_select_tournament()
        return selected_tournament

    def creat_tournament_players(self, tournament_name, number_of_rounds=4):
        number_of_players = int(number_of_rounds) * 2
        print(f"Tournament must have at least {number_of_players} players!")
        answer = "Y"
        i = 0
        while True:
            temp_dict = {}
            answer = input("Want to add more players? (Y/N): ")
            if answer == "N" or answer == "n":
                break
            new_player_obj = self.player_controller_obj.get_player_data()
            self.data.add_player_to_file(new_player_obj)
            player_dict = new_player_obj.__dict__

            temp_dict["player_nid"] = player_dict["national_chess_id"]
            temp_dict["score"] = float(0)

            self.tournament_players_list.append(temp_dict)
            i += 1

        self.data.update_tournament_players(tournament_name, self.tournament_players_list, [])
        return self.tournament_players_list

    def create_match_obj(self, player_score_list):
        player_obj_list = []
        match_obj_list = []
        temp_score_list = []
        # First create player's object list
        for k in range(len(player_score_list)):
            player_obj = None
            data_dict = self.data.get_player_by_code(player_score_list[k]["player_nid"])
            if data_dict:
                player_obj = self.data.create_player_obj(data_dict)
                # print(player_obj.national_chess_id)
                player_obj_list.append(player_obj)
                temp_score_list.append(player_score_list[k]["score"])
            else:
                return None

        # then create match objects from player's object list and score list
        for i in range(0, len(player_obj_list), 2):
            player_1 = player_obj_list[i]
            player_2 = player_obj_list[i+1]
            score_1 = temp_score_list[i]
            score_2 = temp_score_list[i+1]

            # Create Match class object
            match_obj = Match(player_1, score_1, player_2, score_2)
            match_obj_list.append(match_obj.__dict__)

        return match_obj_list

    def add_new_score_to_prev(self, paired_player_list, input_player_score_list):
        new_list = []

        for i in range(len(paired_player_list)):
            temp_dict = {}
            temp_dict["player_nid"] = paired_player_list[i]["player_nid"]
            temp_dict["score"] = float(paired_player_list[i]["score"]) + float(input_player_score_list[i]["score"])
            print(temp_dict["score"])
            new_list.append(temp_dict)
        return new_list

    def update_prev_paired_players(self, paired_player_list):
        temp_list = []
        for i in range(0, len(paired_player_list), 2):
            player1 = paired_player_list[i][0]
            player2 = paired_player_list[i+1][1]
            new_tuple = (player1, player2)
            temp_list.append(new_tuple)
        return temp_list

    def start_round(self, tournament_name, round_number):  # -------------------ROUND 1 ------------------

        # Get round_list from json file if empty
        if not self.round_list:
            self.round_list = self.data.get_rounds_for_tournament(tournament_name)

        # get tournament players list each time
        self.tournament_players_list = self.data.get_tournament_players(tournament_name)

        # get previously paried players in this tournament
        self.previous_paired_players_list = self.data.get_prev_paired_player_list(tournament_name)

        # for first round:
        if round_number == 1:
            # pair randomly returns list of dict
            paired_player_list = self.player_controller_obj.random_pair(self.tournament_players_list)
        # for next round:
        else:
            # pair_players returns list of tuples
            player_tuple_list, score_tuple_list = self.player_controller_obj.pair_players(
                self.tournament_players_list, self.previous_paired_players_list)
            paired_player_list = self.player_controller_obj.merge_list_to_dict(player_tuple_list, score_tuple_list)

            # update set of previously paired players in previous matches
            self.previous_paired_players_list.append(player_tuple_list)

        # print("playing")
        print(fontstyle.apply(f"\n*** Round{round_number} is being played................", "bold"))
        print("---"*10)
        # update round_start_date
        round_start_date = str(datetime.now())
        # round is over
        print(fontstyle.apply(f"*** Round{round_number} is Over!, Enter scores for each player\n", "bold/UNDERLINE"))

        # ask socre for each player for current round
        input_player_score_list = self.view.ask_for_score(paired_player_list)

        # add current score to prev score
        updated_player_score_list = self.add_new_score_to_prev(paired_player_list, input_player_score_list)

        # creat match obj (from tour_playe_list_of dict)
        match_obj_list = self.create_match_obj(updated_player_score_list)

        # sort players and save tourn_player_list
        self.tournament_players_list = self.player_controller_obj.sort_players(updated_player_score_list)

        # update round_end_date and round_number
        round_end_date = str(datetime.now())
        current_round = round_number

        # create round dict
        new_round_dict = {}
        new_round_dict["round_name"] = "Round"+str(round_number)
        new_round_dict["match_list"] = match_obj_list
        new_round_dict["round_start_date"] = round_start_date
        new_round_dict["round_end_date"] = round_end_date

        round_obj = self.data.create_round_obj(new_round_dict)

        # append new object to existing round list
        self.round_list.append(round_obj.__dict__)

        # save updated round_list to json file
        self.data.update_tournament_players(tournament_name, self.tournament_players_list,
                                            self.previous_paired_players_list)
        self.data.update_tournament_rounds(tournament_name, self.round_list, current_round)

    def show_results(self, tournament_name: str):
        print(fontstyle.apply(f"FINAL RESULTS OF Tournament {tournament_name}:\n", "bold/UNDERLINE"))
        print(fontstyle.apply("NAME\t\tNATIONAL CHESS ID\tSCORE", "bold/UNDERLINE"))
        tour_players = self.data.get_tournament_players(tournament_name)
        for i in range(len(tour_players)):
            
            player_dict = self.data.get_player_by_code(tour_players[i]["player_nid"])
            if i == 0:
                winner = player_dict
            format_str = player_dict["last_name"] + " " + player_dict["first_name"] + "\t\t" + \
                tour_players[i]["player_nid"] + "\t\t" + str(tour_players[i]["score"])
            print(format_str)
        win_str = winner["last_name"] + " " + winner["first_name"]
        print(fontstyle.apply(f"*** Winner of the Tournament: '{win_str}'", "bold/UNDERLINE"))
