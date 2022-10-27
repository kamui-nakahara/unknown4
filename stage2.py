import pygame
from stage import Stage
from enemy import Enemy2
from functions import *

class Stage2(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.enemy=Enemy2(self)
        self.items.prob_max=False
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.enemy.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.battery2.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            for bullet in self.battery1.bullets.copy():
                x,y=self.enemy.pos1
                if self.enemy.life[0]>0 and distance(x,y,bullet.x,bullet.y)<=bullet.size+self.enemy.size1:
                    self.battery1.bullets.remove(bullet)
                    self.enemy.life[0]-=1
                x,y=self.enemy.pos2
                if self.enemy.life[1]>0 and distance(x,y,bullet.x,bullet.y)<=bullet.size+self.enemy.size1:
                    self.battery1.bullets.remove(bullet)
                    self.enemy.life[1]-=1
            for bullet in self.battery2.bullets.copy():
                x,y=self.enemy.pos1
                if self.enemy.life[0]>0 and distance(x,y,bullet.x,bullet.y)<=bullet.size+self.enemy.size1:
                    self.battery2.bullets.remove(bullet)
                    self.enemy.life[0]-=1
                x,y=self.enemy.pos2
                if self.enemy.life[1]>0 and distance(x,y,bullet.x,bullet.y)<=bullet.size+self.enemy.size1:
                    self.battery2.bullets.remove(bullet)
                    self.enemy.life[1]-=1
            if self.player.power>self.player.max_power:
                self.player.power=self.player.max_power
            if self.gamestate.damage:
                self.gamestate.damage=False
                self.player.life-=1
                self.enemy.battery.bullets=list()
            if self.gamestate.gameflag=="empty":
                self.lag-=1
            if self.lag<=0:
                self.gamestate.gameflag="nextstage"
    def draw(self):
        self.battery1.draw()
        self.battery2.draw()
        self.enemy.draw()
        self.player.draw()
