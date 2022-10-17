import pygame
from stage import Stage
from enemy import Enemy2

class Stage2(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.enemy=Enemy2(self)
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.enemy.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            if self.player.power>self.player.max_power:
                self.player.power=self.player.max_power
            if self.gamestate.damage:
                self.gamestate.damage=False
                self.player.life-=1
            if self.gamestate.gameflag=="empty":
                self.lag-=1
            if self.lag<=0:
                self.gamestate.gameflag="nextstage"
    def draw(self):
        self.battery1.draw()
        self.enemy.draw()
        self.player.draw()
