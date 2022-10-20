import pygame
from stage import Stage
from enemy import Enemy3
from functions import *

class Stage3(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.enemy=Enemy3(self)
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.battery2.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.enemy.update()
            for bullet in self.battery1.bullets.copy():
                for i in range(self.enemy.amount):
                    if self.enemy.enemys_life[i]>0:
                        x,y=self.enemy.enemys_pos[i]
                        if distance(bullet.x,bullet.y,x,y)<=self.enemy.size1+bullet.size:
                            self.enemy.enemys_life[i]-=1
                            if bullet in self.battery1.bullets:
                                self.battery1.bullets.remove(bullet)
            for bullet in self.battery2.bullets.copy():
                for i in range(self.enemy.amount):
                    if self.enemy.enemys_life[i]>0:
                        x,y=self.enemy.enemys_pos[i]
                        if distance(bullet.x,bullet.y,x,y)<=self.enemy.size1+bullet.size:
                            self.enemy.enemys_life[i]-=1
                            if bullet in self.battery2.bullets:
                                self.battery2.bullets.remove(bullet)
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
