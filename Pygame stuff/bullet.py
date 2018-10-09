import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_Settings,screen,ship):
        """creating bullet at current pos"""
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_Settings.bullet_width,ai_Settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.bullety = float(self.rect.y)

        self.colour = ai_Settings.bullet_colour
        self.bullet_speed_factor = ai_Settings.bullet_speed_factor

    def update(self):
        """move bullet up"""
        self.bullety -= self.bullet_speed_factor
        self.rect.y = self.bullety

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.colour,self.rect)
