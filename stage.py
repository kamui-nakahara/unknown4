import pygame
import sys
from bullet import Battery1

class Stage:
    def __init__(self,main):
        self.gamestate=main.gamestate
        self.settings=main.settings
        self.width=self.settings.display["width"]
        self.height=self.settings.display["height"]
        self.bg_color=self.settings.display["bg_color"]
        self.screen=main.screen
        self.player=main.player
        self.battery1=Battery1(self)
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
        elif key==pygame.K_RETURN:
            self.gamestate.pause=not self.gamestate.pause
        elif key==pygame.K_UP:
            self.player.move_up=True
        elif key==pygame.K_DOWN:
            self.player.move_down=True
        elif key==pygame.K_LEFT:
            self.player.move_left=True
        elif key==pygame.K_RIGHT:
            self.player.move_right=True
        elif key==pygame.K_LSHIFT or key==pygame.K_RSHIFT:
            self.player.move_slow=True
        elif key==pygame.K_z:
            self.battery1.fire=True
    def keyup(self,key):
        if key==pygame.K_UP:
            self.player.move_up=False
        elif key==pygame.K_DOWN:
            self.player.move_down=False
        elif key==pygame.K_LEFT:
            self.player.move_left=False
        elif key==pygame.K_RIGHT:
            self.player.move_right=False
        elif key==pygame.K_LSHIFT or key==pygame.K_RSHIFT:
            self.player.move_slow=False
        elif key==pygame.K_z:
            self.battery1.fire=False
    def update(self):
        pass
    def draw(self):
        pass
