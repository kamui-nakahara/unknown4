import pygame

class Scoreboard:
    def __init__(self,main):
        pygame.font.init()
        self.gamestate=main.gamestate
        self.player=main.player
        self.screen=main.screen
        self.screen_width=main.width
        self.screen_height=main.height
        self.width=main.settings.scoreboard["width"]
        self.bg_color=main.settings.scoreboard["bg_color"]
        self.fg_color=main.settings.scoreboard["fg_color"]
        self.fontsize=main.settings.scoreboard["fontsize"]
        self.rect=pygame.Rect(self.screen_width,0,self.width,self.screen_height)
        self.font=pygame.font.SysFont(None,self.fontsize)
    def update(self,main):
        self.highscore1_text=self.font.render("HIGH SCORE",True,self.fg_color,self.bg_color)
        self.highscore1_rect=self.highscore1_text.get_rect()
        self.highscore1_rect.topleft=(self.screen_width,0)
        self.highscore2_text=self.font.render("{:,}".format(self.gamestate.highscore),True,self.fg_color,self.bg_color)
        self.highscore2_rect=self.highscore2_text.get_rect()
        self.highscore2_rect.topleft=self.highscore1_rect.bottomleft
        self.score_text=self.font.render("SCORE:{:,}".format(self.gamestate.score),True,self.fg_color,self.bg_color)
        self.score_rect=self.score_text.get_rect()
        self.score_rect.topleft=self.highscore2_rect.bottomleft
        self.power_text=self.font.render(f"POWER:{'O'*int(self.player.power)}",True,self.fg_color,self.bg_color)
        self.power_rect=self.power_text.get_rect()
        self.power_rect.topleft=self.score_rect.bottomleft
    def draw(self):
        self.screen.fill(self.bg_color,self.rect)
        self.screen.blit(self.highscore1_text,self.highscore1_rect)
        self.screen.blit(self.highscore2_text,self.highscore2_rect)
        self.screen.blit(self.score_text,self.score_rect)
        self.screen.blit(self.power_text,self.power_rect)
