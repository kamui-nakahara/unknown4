import pygame
from math import *
from enemy import FiringHole
from functions import *
from stage import Stage

class Stage1(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.firinghole=FiringHole(self)
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.battery2.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.firinghole.update(self.gamestate.count,self.player.x,self.player.y)
            for bullet in self.battery1.bullets.copy()+self.battery2.bullets.copy():
                x=bullet.x
                y=bullet.y
                for enemy in self.firinghole.enemys.copy():
                    pos=enemy.pos
                    for [x1,y1],[x2,y2] in zip(pos,pos[1:]+[pos[0]]):
                        if line_hit(x,y,x1,y1,x2,y2,bullet.size):
                            if enemy in self.firinghole.enemys:
                                self.firinghole.enemys.remove(enemy)
                                self.firinghole.items.add(enemy.x,enemy.y)
                                self.gamestate.score+=enemy.points
                                if self.gamestate.highscore<self.gamestate.score:
                                    self.gamestate.highscore=self.gamestate.score
                            if bullet in self.battery1.bullets:
                                self.battery1.bullets.remove(bullet)
            if self.player.power>self.player.max_power:
                self.player.power=self.player.max_power
            if self.gamestate.damage:
                self.gamestate.damage=False
                self.player.life-=1
                self.firinghole.enemys=list()
            if self.gamestate.gameflag=="empty":
                self.lag-=1
            if self.lag<=0:
                self.gamestate.gameflag="nextstage"
    def draw(self):
        self.battery1.draw()
        self.player.draw()
        self.firinghole.draw()
