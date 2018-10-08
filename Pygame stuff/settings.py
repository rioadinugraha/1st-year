class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
     # # Screen settings
        self.screen_width = 500
        self.screen_height = 400
        self.bg_color = (64, 0, 74)
        # ship settings
        self.ship_speed_factor = 1.5
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 100,100,100
