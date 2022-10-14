import pygame
import sys
from math import *
from bullet import Battery1
from enemy import FiringHole
from functions import *

class Stage1:
    def __init__(self,main):
        self.gamestate=main.gamestate
        self.settings=main.settings
        self.width=self.settings.display["width"]
        self.height=self.settings.display["height"]
        self.bg_color=self.settings.display["bg_color"]
        self.screen=main.screen
        self.player=main.player
        self.battery1=Battery1(self)
        self.firinghole=FiringHole(self)
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
        elif key==pygame.K_RETURN:
            self.gamestate.pause=not self.gamestate.pause
        elif key==pygame.K_UP:
            self.player.move_up=True
        elif key==pygame.K_DOWN:
            self.player.move_down=True
        elif key==pygame.K_LEFT:
            self.player.move_left=True
        elif key==pygame.K_RIGHT:
            self.player.move_right=True
        elif key==pygame.K_LSHIFT or key==pygame.K_RSHIFT:
            self.player.move_slow=True
        elif key==pygame.K_z:
            self.battery1.fire=True
    def keyup(self,key):
        if key==pygame.K_UP:
            self.player.move_up=False
        elif key==pygame.K_DOWN:
            self.player.move_down=False
        elif key==pygame.K_LEFT:
            self.player.move_left=False
        elif key==pygame.K_RIGHT:
            self.player.move_right=False
        elif key==pygame.K_LSHIFT or key==pygame.K_RSHIFT:
            self.player.move_slow=False
        elif key==pygame.K_z:
            self.battery1.fire=False
    def update(self):
        if not self.gamestate.pause:
            self.player.update()
            self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
            self.firinghole.update(self.gamestate.count,self.player.x,self.player.y)
            for bullet in self.battery1.bullets.copy():
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
        self.gamestate.count+=1
    def draw(self):
        self.battery1.draw()
        self.player.draw()
        self.firinghole.draw()
