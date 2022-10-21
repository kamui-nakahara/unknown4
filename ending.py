import pygame
import sys
from stage import Stage

class Ending(Stage):
    def __init__(self,main):
        super().__init__(main)
        pygame.font.init()
        self.font=pygame.font.SysFont(None,40)
        self.end_text=self.font.render("made by Kamui-Nakahara",True,(255,255,255),self.bg_color)
        self.end_rect=self.end_text.get_rect()
        self.end_rect.center=(self.width/2,0)
        self.end_rect.top=self.height
        self.y=self.height
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
        elif key==pygame.K_RETURN:
            self.next()
    def keyup(self,key):
        pass
    def update(self):
        self.y-=1
        self.end_rect.top=self.y
        if self.end_rect.bottom<0:
            self.next()
    def draw(self):
        self.screen.blit(self.end_text,self.end_rect)
    def next(self):
        self.gamestate.gameflag="restart"
