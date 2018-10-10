import sys
from button import Button
import pygame
from settings import Settings
from ship import Ship
from enemies import Alien
from pygame.sprite import Group
from game_Stats import GameStats
import game_functions as gf
from scoreboard import scoreboard
def run_game():
 # Initialize game and create a screen object.
    pygame.init()
    ai_Setting = Settings()
    screen = pygame.display.set_mode((ai_Setting.screen_width, ai_Setting.screen_height))
    pygame.display.set_caption("Alien Invasion mofo")
    stats = GameStats(ai_Setting)
    sb = scoreboard(ai_Setting,screen,stats)
    alien = Alien(ai_Setting,screen)
    bg_music = ai_Setting.bg_music
    bg_music.set_volume(0.4)
    bg_music.play(-1)
    # make a ship
    ship = Ship(ai_Setting,screen)
    play_button =Button(ai_Setting,screen,"play")
    screen.blit(ai_Setting.bg,[0,0])
    bullets = Group()
    aliens = Group()
    # Start the main loop for the  game.
    gf.create_fleet(ai_Setting, screen, ship, aliens)
    # create the fleet of aliens

    while True:
        gf.check_events(ai_Setting,screen,stats,sb,play_button,ship,aliens,bullets)

    # Watch for keyboard and mouse events.
        if stats.game_active:
            screen.blit(ai_Setting.bg,[0,0])
            ship.update()
            gf.update_bullets(ai_Setting,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_Setting,stats,screen,sb,ship,aliens,bullets)

        gf.update_screen(ai_Setting,screen,stats,sb,ship,aliens,bullets,play_button)



 # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
