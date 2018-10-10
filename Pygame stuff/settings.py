import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""


    def __init__(self):
        """Initialize the game's settings."""
     # # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg = pygame.image.load('C:\\untitled\\First work\\Pygame stuff\\images\\nier.jpg')
        # ship settings
        self.ship_speed_factor = 3
        self.ship_limit = 2
        #bullet settings
        self.bullet_speed_factor = 5
        self.bullets_allowed = 3
        self.bullets_sound = pygame.mixer.Sound('C:\\untitled\\First work\\Pygame stuff\\images\\laset.wav')
        #alineu settingu
        self.alien_Speed_factor =2
        self.fleet_drop_Speed = 10
        #1 = right, -1=left
        self.fleet_direction =1


