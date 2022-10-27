import pygame
from stage import Stage
from enemy import Enemy5
from functions import *

class Stage5(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.enemy=Enemy5(self)
        self.items.prob_max=True
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.battery2.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.enemy.update()
            pos1=self.enemy.pos1
            pos2=self.enemy.pos2
            for bullet in self.battery1.bullets.copy():
                if not (0<=bullet.x<=self.width and 0<=bullet.y<=self.height):
                    self.battery1.bullets.remove(bullet)
                    continue
                x=bullet.x
                y=bullet.y
                if self.enemy.life>0 and True in [True for [x1,y1],[x2,y2] in zip(pos1,pos1[1:]+[pos1[0]]) if line_hit(x,y,x1,y1,x2,y2,self.player.coll)]:
                    self.battery1.bullets.remove(bullet)
                    self.enemy.life-=1
                    continue
                if self.enemy.life>0 and True in [True for [x1,y1],[x2,y2] in zip(pos2,pos2[1:]+[pos2[0]]) if line_hit(x,y,x1,y1,x2,y2,self.player.coll)]:
                    self.battery1.bullets.remove(bullet)
                    self.enemy.life-=1
                    continue
                bullet.update()
            for bullet in self.battery2.bullets.copy():
                if not (0<=bullet.x<=self.width and 0<=bullet.y<=self.height):
                    self.battery2.bullets.remove(bullet)
                    continue
                x=bullet.x
                y=bullet.y
                if self.enemy.life>0 and True in [True for [x1,y1],[x2,y2] in zip(pos1,pos1[1:]+[pos1[0]]) if line_hit(x,y,x1,y1,x2,y2,self.player.coll)]:
                    self.battery2.bullets.remove(bullet)
                    self.enemy.life-=1
                    continue
                if self.enemy.life>0 and True in [True for [x1,y1],[x2,y2] in zip(pos2,pos2[1:]+[pos2[0]]) if line_hit(x,y,x1,y1,x2,y2,self.player.coll)]:
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
