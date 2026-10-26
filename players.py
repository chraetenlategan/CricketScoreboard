class PlayerStats:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls_faced = 0
        self.fours = 0
        self.sixes = 0
        self.is_out = False
        self.strike = False
        self.strike_rate = 0.0
        self.dismissal_info = ""