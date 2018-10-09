import sys
import pygame
from settings import Settings
from ship import Ship
from enemies import Alien
from pygame.sprite import Group
import game_functions as gf

def run_game():
 # Initialize game and create a screen object.
    pygame.init()
    ai_Setting = Settings()
    screen = pygame.display.set_mode((ai_Setting.screen_width, ai_Setting.screen_height))
    pygame.display.set_caption("Alien Invasion mofo")
    alien = Alien(ai_Setting,screen)
    # make a ship
    ship = Ship(ai_Setting,screen)
    bullets = Group()
    aliens = Group()
    # Start the main loop for the  game.
    gf.create_fleet(ai_Setting, screen, ship, aliens)
    # create the fleet of aliens
    while True:
    # Watch for keyboard and mouse events.
        gf.check_events(ai_Setting,screen,ship,bullets)
        ship.update()

        # print("Left : "+str(ship.moving_left))
        # print("Right : "+str(ship.moving_right))

        gf.update_bullets(bullets)
        gf.update_screen(ai_Setting,screen,ship,aliens,bullets)



 # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
