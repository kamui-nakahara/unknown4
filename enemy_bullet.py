import pygame
from math import sin,cos,radians
from functions import *

class Battery1:
    def __init__(self,enemy):
        self.gamestate=enemy.gamestate
        self.screen=enemy.screen
        self.width=enemy.screen_width
        self.height=enemy.screen_height
        self.size1=enemy.settings["size1"]
        self.size2=enemy.settings["size2"]
        self.color1=enemy.settings["color1"]
        self.color2=enemy.settings["color2"]
        self.speed=enemy.settings["speed"]
        self.timing=enemy.settings["timing"]
        self.interval1=enemy.settings["interval1"]
        self.interval2=enemy.settings["interval2"]
        self.angle_step=enemy.settings["angle_step"]
        self.append_rate=enemy.settings["append_rate"]
        self.player=enemy.player
        self.bullets=list()
        self.pos1=enemy.pos1
        self.pos2=enemy.pos2
        self.enemy=enemy
        self.count=0
    def add(self):
        for i in range(0,360,self.angle_step):
            if self.enemy.life[0]>0:
                bullet=Bullet1(self,*self.pos1,i+self.count*self.append_rate)
                self.bullets+=[bullet]
            if self.enemy.life[1]>0:
                bullet=Bullet1(self,*self.pos2,-(i+self.count*self.append_rate))
                self.bullets+=[bullet]
        self.count+=1
    def update(self):
        count=self.gamestate.count%(self.interval1+self.interval2)
        if count<=self.interval1 and self.gamestate.count%self.timing==0:
            self.add()
        for bullet in self.bullets.copy():
            if 0<=bullet.x<=self.width and 0<=bullet.y<=self.height:
                bullet.update()
            else:
                self.bullets.remove(bullet)
            if distance(bullet.x,bullet.y,self.player.x,self.player.y)<=bullet.size1+self.player.coll:
                self.gamestate.damage=True
                break
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

class Bullet1:
    def __init__(self,battery,x,y,angle):
        self.screen=battery.screen
        self.size1=battery.size1
        self.size2=battery.size2
        self.color1=battery.color1
        self.color2=battery.color2
        self.speed=battery.speed
        self.vx=cos(radians(angle))*self.speed
        self.vy=sin(radians(angle))*self.speed
        self.x=x
        self.y=y
    def update(self):
        self.x+=self.vx
        self.y+=self.vy
    def draw(self):
        pygame.draw.circle(self.screen,self.color1,(self.x,self.y),self.size1)
        pygame.draw.circle(self.screen,self.color2,(self.x,self.y),self.size2)
