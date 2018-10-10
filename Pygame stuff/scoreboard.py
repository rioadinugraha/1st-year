import pygame.font
from pygame.sprite import Group
from lives import lives
class scoreboard():

    def __init__(self,ai_Setting, screen,stats):
        """initialize scroekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_Setting
        self.stats = stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_Score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        rounded_Score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_Score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top =20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_Score_image,self.high_Score_Rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
    def prep_high_Score(self):
        """turn highscore into image"""
        high_Score = int(round(self.stats.high_Score,-1))
        high_score_str = "{:,}".format(high_Score)
        self.high_Score_image = self.font.render(high_score_str,True,
                    self.text_color,self.ai_settings.bg)
        self.high_Score_Rect = self.high_Score_image.get_rect()
        self.high_Score_Rect.centerx = self.screen_rect.centerx
        self.high_Score_Rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level),True,
                                            self.text_color, self.ai_settings.bg)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom +10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range (self.stats.ships_left):
            ship = lives(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

