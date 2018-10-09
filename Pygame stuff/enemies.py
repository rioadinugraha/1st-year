import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """initialize the alien and set it's starting position"""

    def __init__(self,ai_Settings,screen):
        """initiialize it and set its position"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_Settings = ai_Settings

        # load the image
        self.image = pygame.image.load('C:\\untitled\\First work\\Pygame stuff\\images\\alienu.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)


