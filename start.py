import pygame
import sys
from stage import Stage

class Start(Stage):
    def __init__(self,main):
        super().__init__(main)
        pygame.font.init()
        self.font=pygame.font.SysFont(None,50)
        self.start_text=self.font.render("PRESS ENTER",True,(255,255,255),self.bg_color)
        self.start_rect=self.start_text.get_rect()
        self.start_rect.center=(self.width/2,self.height/2)
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
        elif key==pygame.K_RETURN:
            self.gamestate.gameflag="nextstage"
    def keyup(self,key):
        pass
    def draw(self):
        self.screen.blit(self.start_text,self.start_rect)
