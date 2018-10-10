import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_Settings,screen,ship):
        """creating bullet at current pos"""
        super(Bullet,self).__init__()
        self.screen = screen

        self.image = pygame.image.load('C:\\untitled\\First work\\Pygame stuff\\images\\bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.bullety = float(self.rect.y)

        self.bullet_speed_factor = ai_Settings.bullet_speed_factor

    def update(self):
        """move bullet up"""
        self.bullety -= self.bullet_speed_factor
        self.rect.y = self.bullety

    def draw_bullet(self):
        """draw the bullet to the screen"""
        self.screen.blit(self.image,self.rect)
