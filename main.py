import pygame
import sys
from settings import Settings
from player import Player

class Main:
    def __init__(self):
        self.settings=Settings()
        self.width=self.settings.display["width"]
        self.height=self.settings.display["height"]
        self.bg_color=self.settings.display["bg_color"]
        self.screen=pygame.display.set_mode((self.width,self.height))
    def loop(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self.keydown(event.key)
            elif event.type==pygame.KEYUP:
                self.keyup(event.key)
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
        elif key==pygame.K_UP:
            pass
        elif key==pygame.K_DOWN:
            pass
        elif key==pygame.K_LEFT:
            pass
        elif key==pygame.K_RIGHT:
            pass
    def keyup(self,key):
        if key==pygame.K_UP:
            pass
        elif key==pygame.K_DOWN:
            pass
        elif key==pygame.K_LEFT:
            pass
        elif key==pygame.K_RIGHT:
            pass
    def update(self):
        pass
    def draw(self):
        self.screen.fill(self.bg_color)
        pygame.display.update()
if __name__=="__main__":
    main=Main()
    main.loop()
