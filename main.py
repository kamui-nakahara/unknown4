#!/Users/kamui-nakahara/.pyenv/shims/python
import pygame
from settings import Settings
from player import Player
from scoreboard import Scoreboard
from start import Start
from stage1 import Stage1
from stage2 import Stage2
from stage3 import Stage3
from stage4 import Stage4
from ending import Ending
from gameover import Gameover
from gamestate import Gamestate
from item import Items1
from bullet import Battery1,Battery2

class Main:
    def __init__(self):
        self.settings=Settings()
        self.width=self.settings.display["width"]
        self.height=self.settings.display["height"]
        self.screen=pygame.display.set_mode((self.width+self.settings.scoreboard["width"],self.height))
        self.gamestate=Gamestate()
        self.player=Player(self)
        self.battery1=Battery1(self)
        self.battery2=Battery2(self)
        self.items=Items1(self,self.settings.item1,self.player)
        self.stages=self.nextstage()
        self.stage=next(self.stages)(self)
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
    def nextstage(self):
        for i in [Start,Stage1,Stage2,Stage3,Stage4,Ending]:
            yield i
    def update(self):
        if self.gamestate.gameflag=="gameover":
            self.stage=Gameover(self)
        elif self.gamestate.gameflag=="nextstage":
            self.stage=next(self.stages)(self)
            self.gamestate.gameflag="playing"
        elif self.gamestate.gameflag=="restart":
            self.gamestate=Gamestate()
            self.player=Player(self)
            self.battery1=Battery1(self)
            self.battery2=Battery2(self)
            self.items=Items1(self,self.settings.item1,self.player)
            self.stages=self.nextstage()
            self.stage=next(self.stages)(self)
            self.scoreboard=Scoreboard(self)
        self.stage.update()
        self.scoreboard.update(self)
        self.gamestate.count+=1
    def draw(self):
        self.screen.fill(self.stage.bg_color)
        self.stage.draw()
        self.scoreboard.draw()
        pygame.display.update()
if __name__=="__main__":
    main=Main()
    main.loop()
