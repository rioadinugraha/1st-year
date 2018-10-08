import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
 # Initialize game and create a screen object.
    pygame.init()
    ai_Setting = Settings()
    screen = pygame.display.set_mode((ai_Setting.screen_width, ai_Setting.screen_height))
    pygame.display.set_caption("Alien Invasion mofo")

    # make a ship
    ship = Ship(ai_Setting,screen)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_Setting,screen,ship)
 # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
