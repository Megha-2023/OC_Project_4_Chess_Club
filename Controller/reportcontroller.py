import fontstyle
from datetime import datetime


class ReportController:
    def __init__(self, view, data):
        self.view = view
        self.data = data

    # list of all players, sorted alphabatically
    def show_all_players(self):
        players_list = self.data.get_all_players_data()
        players_list.sort(key=lambda x: x['last_name'])
        print(fontstyle.apply("NAME\t\t(National Chess ID)", "bold/UNDERLINE"))
        for player in players_list:
            format_str = player["last_name"] + " " + player["first_name"] + "\t(" + player["national_chess_id"] + ")"
            print(format_str)

    # list fo all tournamets
    def show_all_tournaments(self):
        all_tour = self.data.get_all_tournament_data()
        print(fontstyle.apply("NAME\tPLACE", "bold/UNDERLINE"))
        for tour in all_tour:
            format_str = tour["tournament_name"] + "\t" + tour["tournament_place"]
            print(format_str)

    # name and dates of given tournamene
    def show_name_date_tour(self, tournament_name):
        tour = self.data.get_selected_tournament(tournament_name)
        print("\nTOURNAMENT NAME:\t", tour["tournament_name"])
        print("TOURNAMENT PLACE:\t", tour["tournament_place"])

        date_obj = datetime.strptime(tour["tournament_start_date"], "%Y-%m-%d")
        print("TOURNAMENT START DATE:\t", date_obj.strftime("%d-%m-%Y"))

        date_obj = datetime.strptime(tour["tournament_end_date"], "%Y-%m-%d")
        print("TOURNAMENT END DATE:\t", date_obj.strftime("%d-%m-%Y"))

    # list of players in tournament, sorted alphabetically
    def show_tournament_players(self, tournament_name):
        new_list = []
        tour_players = self.data.get_tournament_players(tournament_name)
        for player in tour_players:
            player_dict = self.data.get_player_by_code(player["player_nid"])
            new_list.append(player_dict)
        new_list.sort(key=lambda x: x["last_name"])
        print(fontstyle.apply(f"\nPlayers participating in Tournament {tournament_name}", "bold/UNDERLINE"))
        print(fontstyle.apply("NAME\t\t(National Chess ID)", "bold/UNDERLINE"))
        for player in new_list:
            format_str = player["last_name"] + " " + player["first_name"] + "\t(" + player["national_chess_id"] + ")"
            print(format_str)

    # list of all rounds in tournament and all matches
    def show_rounds_matches(self, tournament_name):
        round_list = self.data.get_rounds_for_tournament(tournament_name)
        for item in round_list:
            print(fontstyle.apply(f"\n\t{item['round_name']}", "bold"))
            i = 1
            for match in item["match_list"]:
                print(f"Match {i}: ", match["match"])
                i += 1
