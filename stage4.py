import pygame
from stage import Stage
from enemy import Enemy4
from functions import *

class Stage4(Stage):
    def __init__(self,main):
        super().__init__(main)
        self.enemy=Enemy4(self)
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.battery2.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.enemy.update()
            pos=self.enemy.pos
            for bullet in self.battery1.bullets.copy():
                if not (0<=bullet.x<=self.width and 0<=bullet.y<=self.height):
                    self.battery1.bullets.remove(bullet)
                    continue
                x=bullet.x
                y=bullet.y
                if True in [True for [x1,y1],[x2,y2] in zip(pos,pos[1:]+[pos[0]]) if line_hit(x,y,x1,y1,x2,y2,self.player.coll)]:
                    self.battery1.bullets.remove(bullet)
                    continue
                bullet.update()
            for bullet in self.battery2.bullets.copy():
                if not (0<=bullet.x<=self.width and 0<=bullet.y<=self.height):
                    self.battery2.bullets.remove(bullet)
                    continue
                x=bullet.x
                y=bullet.y
                if True in [True for [x1,y1],[x2,y2] in zip(pos,pos[1:]+[pos[0]]) if line_hit(x,y,x1,y1,x2,y2,self.player.coll)]:
                    self.battery2.bullets.remove(bullet)
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
        self.enemy.draw()
        self.player.draw()
