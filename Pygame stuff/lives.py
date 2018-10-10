import pygame
from pygame.sprite import Sprite

class lives(Sprite):

    def __init__(self,ai_Settings,screen):
        """initialize the ship and set its starting position"""
        self.screen = screen

        super(lives,self).__init__()

        self.ai_Settings = ai_Settings
        # load the ship image and get its rect.
        self.image = pygame.image.load('C:\\untitled\\First work\\Pygame stuff\\images\\planes.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
