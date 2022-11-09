import pygame
from stage import Stage
from enemy import Enemy6
from functions import *

class Stage6(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.enemy=Enemy6(self)
        self.items.prob_max=True
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.battery2.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.enemy.update()
            for bullet in self.battery1.bullets:
                if not (0<=bullet.x<=self.width and 0<=bullet.y<=self.height):
                    self.battery1.bullets.remove(bullet)
                    continue
                if self.gamestate.gameflag=="playing" and distance(self.enemy.x,self.enemy.y,bullet.x,bullet.y)<self.enemy.size+bullet.size:
                    self.battery1.bullets.remove(bullet)
                    self.enemy.life-=1
                    continue
                bullet.update()
            for bullet in self.battery2.bullets:
                if not (0<=bullet.x<=self.width and 0<=bullet.y<=self.height):
                    self.battery2.bullets.remove(bullet)
                    continue
                if self.gamestate.gameflag=="playing" and distance(self.enemy.x,self.enemy.y,bullet.x,bullet.y)<self.enemy.size+bullet.size:
                    self.battery2.bullets.remove(bullet)
                    self.enemy.life-=1
                    continue
                bullet.update()
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
        self.battery2.draw()
        self.player.draw()
        self.enemy.draw()
