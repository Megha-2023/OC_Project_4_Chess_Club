# from Models.data import Data
from Models.filedata import FileData
from Views.view import View
from Controller.maincontroller import MainController
from Controller.tourna_controller import TournamentController
from Controller.playercontroller import PlayerController
from reportcontroller import ReportController


def main():
    view_obj = View()
    data_obj = FileData()
    player_contr_obj = PlayerController(view_obj, data_obj)
    tournament_contr_obj = TournamentController(view_obj, data_obj, player_contr_obj)
    report_contr_obj = ReportController(view_obj, data_obj)
    main_contr = MainController(view_obj, tournament_contr_obj, data_obj, player_contr_obj, report_contr_obj)
    
    main_contr.display_main_menu()


if __name__ == "__main__":
    main()
