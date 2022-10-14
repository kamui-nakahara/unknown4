import pygame
from settings import Settings
from player import Player
from scoreboard import Scoreboard
from stage1 import Stage1
from gameover import Gameover
from gamestate import Gamestate

class Main:
    def __init__(self):
        self.settings=Settings()
        self.width=self.settings.display["width"]
        self.height=self.settings.display["height"]
        self.screen=pygame.display.set_mode((self.width+self.settings.scoreboard["width"],self.height))
        self.gamestate=Gamestate()
        self.player=Player(self)
        self.stage=Stage1(self)
        self.scoreboard=Scoreboard(self)
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
                self.stage.keydown(event.key)
            elif event.type==pygame.KEYUP:
                self.stage.keyup(event.key)
    def update(self):
        if self.gamestate.gameflag=="gameover":
            self.stage=Gameover(self)
        elif self.gamestate.gameflag=="nextstage":
            pass
        self.stage.update()
        self.scoreboard.update(self)
    def draw(self):
        self.screen.fill(self.stage.bg_color)
        self.stage.draw()
        self.scoreboard.draw()
        pygame.display.update()
if __name__=="__main__":
    main=Main()
    main.loop()
