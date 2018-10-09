import pygame

class Ship():

    def __init__(self,ai_Settings,screen):
        """initialize the ship and set its starting position"""
        self.screen = screen

        self.ai_Settings = ai_Settings
        # load the ship image and get its rect.
        self.image = pygame.image.load('C:\\untitled\\First work\\Pygame stuff\\images\\spasu.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # store a decimal for ship center
        self.centerX = float(self.rect.centerx)
        self.centerY =float(self.rect.centery)
        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """update the ship's position based on the movement flag"""

        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.centerX += self.ai_Settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerX -= self.ai_Settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centerY -= self.ai_Settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.ai_Settings.ship_speed_factor

        # update rect object from self.center.
        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY

    def blitme(self):
        """draw ship at its current location."""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.centerX = self.screen_rect.centerx
        self.centerY = self.screen_rect.bottom - self.rect.height/2


