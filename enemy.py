import pygame
from math import sin,cos,radians

class FiringHole:
    def __init__(self,main):
        self.screen=main.screen
        self.width=main.width
        self.height=main.height
        self.size=main.settings.enemy1["size"]
        self.color=main.settings.enemy1["color"]
        self.speed=main.settings.enemy1["speed"]
        self.timing=main.settings.enemy1["timing"]
        self.height1=main.settings.enemy1["height1"]
        self.height2=main.settings.enemy1["height2"]
        self.enemys=list()
    def add1(self):
        x=0
        y=self.height1
        enemy=Enemy1(self,x,y,0)
        self.enemys+=[enemy]
    def update(self,count):
        if count%self.timing==0:
            self.add1()
        for enemy in self.enemys.copy():
            if True in [(0<=x<=self.width and 0<=y<=self.height) for x,y in enemy.pos]:
                enemy.update()
            else:
                self.enemys.remove(enemy)
    def draw(self):
        for enemy in self.enemys:
            enemy.draw()
class Enemy1:
    def __init__(self,firinghole,x,y,angle):
        self.screen=firinghole.screen
        self.width=firinghole.width
        self.size=firinghole.size
        self.color=firinghole.color
        self.speed=firinghole.speed
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
    def update(self):
        if self.x>self.width/2 and not self.flag:
            self.turn_flag=not self.turn_flag
        self.flag=self.x>self.width/2
        if self.turn_flag:
            self.angle-=self.speed/2
        vx=cos(radians(self.angle))*self.speed
        vy=sin(radians(self.angle))*self.speed
        self.x+=vx
        self.y+=vy
        self.update_pos()
    def draw(self):
        pygame.draw.polygon(self.screen,self.color,self.pos)
