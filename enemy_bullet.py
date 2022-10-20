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

class Battery2:
    def __init__(self,enemy):
        self.gamestate=enemy.gamestate
        self.screen=enemy.screen
        self.width=enemy.screen_width
        self.height=enemy.screen_height
        self.settings=enemy.settings
        self.timing=enemy.settings["timing"]
        self.player=enemy.player
        self.enemy=enemy
        self.bullets=list()
    def add(self):
        for i in range(self.enemy.amount):
            if self.enemy.enemys_life[i]>0:
                angle=i*360/self.enemy.amount+self.enemy.angle
                for j in range(0,360,90):
                    bullet=Bullet2(self,angle+j,self.enemy.enemys_pos[i])
                    self.bullets+=[bullet]
    def update(self):
        if self.gamestate.count%self.timing==0:
            self.add()
        x=self.player.x
        y=self.player.y
        for bullet in self.bullets.copy():
            if not (0<=bullet.x<=self.width and 0<=bullet.y<=self.height):
                self.bullets.remove(bullet)
                continue
            pos=bullet.pos
            if True in [True for [x1,y1],[x2,y2] in zip(pos,pos[1:]+[pos[0]]) if line_hit(x,y,x1,y1,x2,y2,self.player.coll)]:
                self.gamestate.damage=True
                self.bullets=list()
                break
            bullet.update()
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
class Bullet2:
    def __init__(self,battery,angle,pos):
        self.gamestate=battery.gamestate
        self.screen=battery.screen
        self.size1=battery.settings["size1"]
        self.size2=battery.settings["size2"]
        self.color=battery.settings["color"]
        self.speed=battery.settings["speed"]
        self.angle=angle
        self.vx=cos(radians(angle))*self.speed
        self.vy=sin(radians(angle))*self.speed
        self.x,self.y=pos
        self.pos=list()
        self.update_pos()
        self.count=battery.gamestate.count
    def update_pos(self):
        self.pos=[
                (cos(radians(self.angle))*self.size1+self.x,sin(radians(self.angle))*self.size1+self.y),
                (cos(radians(self.angle+90))*self.size2+self.x,sin(radians(self.angle+90))*self.size2+self.y),
                (cos(radians(self.angle+180))*self.size1+self.x,sin(radians(self.angle+180))*self.size1+self.y),
                (cos(radians(self.angle+270))*self.size2+self.x,sin(radians(self.angle+270))*self.size2+self.y)]
    def update(self):
        self.x+=self.vx
        self.y+=self.vy
        self.update_pos()
        if self.count!=-1 and self.gamestate.count-self.count>70:
            self.vy=-self.vy*2
            self.count=-1
    def draw(self):
        pygame.draw.polygon(self.screen,self.color,self.pos)
