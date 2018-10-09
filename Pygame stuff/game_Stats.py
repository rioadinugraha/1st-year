class GameStats():

    def __init__(self,setting):
        self.ai_Settings = setting
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_Settings.ship_limit


