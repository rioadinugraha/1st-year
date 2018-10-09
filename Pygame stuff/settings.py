class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
     # # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (64, 0, 74)
        # ship settings
        self.ship_speed_factor = 1.5
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_colour = 100,100,100
        self.bullets_allowed = 3

