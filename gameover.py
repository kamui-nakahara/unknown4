import pygame
import sys
from stage import Stage

class Gameover(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.bg_color=main.settings.gameover["bg_color"]
        self.fg_color1=main.settings.gameover["fg_color1"]
        self.fontsize1=main.settings.gameover["fontsize1"]
        self.font1=pygame.font.SysFont(None,self.fontsize1)
        self.render()
    def render(self):
        self.gameover_text=self.font1.render("GAME OVER",True,self.fg_color1,self.bg_color)
        self.gameover_rect=self.gameover_text.get_rect()
        self.gameover_rect.center=(self.width/2,self.height/2)
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
    def keyup(self,key):
        pass
    def draw(self):
        self.screen.blit(self.gameover_text,self.gameover_rect)
