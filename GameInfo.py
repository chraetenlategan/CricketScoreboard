class GetGameInfo:
    def __init__(self):
        self.formats = {
            1: "T20",
            2: "ODI"
        }
        self.overs = 0
        self.is_valid_input = False

    def get_format(self):
        while not self.is_valid_input:
            try:
                format_chosen = int(input(f"Please choose a format : {self.formats} \n"))
                if format_chosen == 1:
                    self.overs = 20
                    self.is_valid_input = True
                elif format_chosen == 2:
                    self.overs = 50
                    self.is_valid_input = True
                else:
                    print("Please do enter a valid input.")
            except ValueError:
                print("Please do enter a valid input.")

    def get_team_names(self):
        team1 = input("Please enter the name of team 1: ")
        team2 = input("Please enter the name for team 2: ")
        return team1, team2

    def get_player_names(self):
        team1_players = []
        team2_players = []
        print("Let's get the batting order")

        for i in range(1, 12):
            team1_players.append(input(f"Please do enter name for batsman {i}: "))

        for i in range(1, 12):
            team2_players.append(input(f"Please do enter name for batsman {i}: "))

        return team1_players, team2_players