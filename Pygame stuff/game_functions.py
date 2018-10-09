import sys

import pygame

from bullet import Bullet
from enemies import Alien
from time import sleep

def check_keydown_events(event,ai_Settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        #move the ship to the right.
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key ==pygame.K_SPACE:
        fire_bullet(ai_Settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_Settings,screen, ship, bullets):
    """fire a bullet if limit not reached yet."""
    if len(bullets) < ai_Settings.bullets_allowed:
            new_bullet = Bullet(ai_Settings,screen,ship)
            bullets.add(new_bullet)


def update_bullets(ai_Setting, screen, ship, aliens, bullets):
    """update position of bullets and get rid of old bullets"""
    bullets.update()
    #get rid of em
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    check_bullet_alien_collisions(ai_Setting,screen,ship,aliens,bullets)
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        #move the ship to the right.
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_Settings,screen,ship,bullets):
    """respond to stuff"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_Settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship,alien,bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def create_fleet(ai_Setting,screen,ship,aliens):
    """creating fleets of aliens"""
    alien = Alien(ai_Setting,screen)
    number_aliens_x = get_number_aliens_x(ai_Setting,alien.rect.width)
    number_rows = get_number_rows(ai_Setting,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_Setting,screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_Setting,alien_width):
    space_for_alien = ai_Setting.screen_width - 2 * alien_width
    number_aliens_x = int(space_for_alien / (2*alien_width))
    return number_aliens_x

def create_alien(ai_Setting,screen,aliens, alien_number,row_number):
    alien = Alien(ai_Setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_Setting,ship_height,alien_height):
    available_Space_y = (ai_Setting.screen_height - (2*alien_height) - ship_height)
    number_rows = int(available_Space_y/(2*alien_height))
    return number_rows

def update_aliens(ai_Settings,stats,screen,ship, aliens,bullets):
    check_fleet_edges(ai_Settings,aliens)
    aliens.update()

    # ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_Settings,stats,screen,ship,aliens,bullets)

    check_aliens_bottom(ai_Settings,stats,screen,ship,aliens,bullets)
def check_fleet_edges(ai_Setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_Fleet_Direction(ai_Setting,aliens)
            break
def change_Fleet_Direction(ai_Settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_Settings.fleet_drop_Speed
    ai_Settings.fleet_direction*= -1

def check_bullet_alien_collisions(ai_Settings,screen,ship,aliens,bullets):
 collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

 if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_Settings,screen,ship,aliens)

def ship_hit(ai_Settings,stats,screen,ship,aliens,bullets):
    stats.ships_left -=1
    if stats.ships_left >0:

        aliens.empty()
        bullets.empty()

        create_fleet(ai_Settings,screen,ship,aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break
