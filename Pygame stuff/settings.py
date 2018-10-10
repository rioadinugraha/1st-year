import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""


    def __init__(self):
        """Initialize the game's settings."""
     # # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg = pygame.image.load('C:\\untitled\\First work\\Pygame stuff\\images\\nier.jpg')
        self.bg_music = pygame.mixer.Sound('C:\\untitled\\First work\\Pygame stuff\\images\\bgmusic.wav')
        # ship settings
        self.ship_speed_factor = 3
        self.ship_limit = 2
        #bullet settings
        self.bullets_allowed = 7
        self.bullets_sound = pygame.mixer.Sound('C:\\untitled\\First work\\Pygame stuff\\images\\laset.wav')
        #alineu settingu
        self.fleet_drop_Speed = 10
        #1 = right, -1=left
        #speedo increase
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()
        #score increase
        self.score_scale =1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 5
        self.alien_Speed_factor = 2

        #fleet d
        self.fleet_direction =1
        self.alien_points = 50

    def increase_Speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_Speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

