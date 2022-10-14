import pygame
from math import sin,cos,radians
from item import Items1
from functions import *

class FiringHole:
    def __init__(self,main):
        self.gamestate=main.gamestate
        self.screen=main.screen
        self.screen_width=main.width
        self.screen_height=main.height
        self.size=main.settings.enemy1["size"]
        self.color=main.settings.enemy1["color"]
        self.speed=main.settings.enemy1["speed"]
        self.timing=main.settings.enemy1["timing"]
        self.height=main.settings.enemy1["height"]
        self.points=main.settings.enemy1["points"]
        self.player_size=main.player.coll
        self.items=Items1(self,main.settings.item1,main.player)
        self.flag=False
        self.enemys=list()
    def add(self):
        x=0
        y=self.height
        enemy=Enemy1(self,x,y,0)
        self.enemys+=[enemy]
    def update(self,count,x,y):
        if count%self.timing==0:
            self.add()
        for enemy in self.enemys.copy():
            if True in [(0<=x<=self.screen_width and 0<=y<=self.screen_height) for x,y in enemy.pos]:
                enemy.update(count,x,y)
            else:
                self.enemys.remove(enemy)
        if self.flag:
            self.height+=10
            if self.height>400:
                self.flag=False
        else:
            self.height-=10
            if self.height<200:
                self.flag=True
        self.items.update()
    def draw(self):
        self.items.draw()
        for enemy in self.enemys:
            enemy.draw()
class Enemy1:
    def __init__(self,firinghole,x,y,angle):
        self.gamestate=firinghole.gamestate
        self.screen=firinghole.screen
        self.screen_width=firinghole.screen_width
        self.size=firinghole.size
        self.color=firinghole.color
        self.speed=firinghole.speed
        self.points=firinghole.points
        self.player_size=firinghole.player_size
        self.x=x
        self.y=y
        self.angle=angle
        self.turn_angle=self.angle-90-360
        self.pos=[]
        self.turn_flag=False
        self.flag=False
        self.update_pos()
    def update_pos(self):
        self.pos=[
                [cos(radians(self.angle+20))*self.size+self.x,
                    sin(radians(self.angle+20))*self.size+self.y],
                [cos(radians(self.angle+160))*self.size+self.x,
                    sin(radians(self.angle+160))*self.size+self.y],
                [cos(radians(self.angle+200))*self.size+self.x,
                    sin(radians(self.angle+200))*self.size+self.y],
                [cos(radians(self.angle+340))*self.size+self.x,
                    sin(radians(self.angle+340))*self.size+self.y]
                ]
    def update(self,count,x,y):
        if self.x>self.screen_width/2 and not self.flag:
            self.turn_flag=not self.turn_flag
        self.flag=self.x>self.screen_width/2
        if self.turn_flag:
            self.angle-=self.speed/2
        vx=cos(radians(self.angle))*self.speed
        vy=sin(radians(self.angle))*self.speed
        self.x+=vx
        self.y+=vy
        self.update_pos()
        for [x1,y1],[x2,y2] in zip(self.pos,self.pos[1:]+[self.pos[0]]):
            if line_hit(x,y,x1,y1,x2,y2,self.player_size):
                self.gamestate.damage=True
    def draw(self):
        pygame.draw.polygon(self.screen,self.color,self.pos)