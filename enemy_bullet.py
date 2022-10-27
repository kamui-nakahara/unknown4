import pygame
from math import tan,sin,cos,radians
from random import randint
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

class Battery3:
    def __init__(self,enemy):
        self.gamestate=enemy.gamestate
        self.player=enemy.player
        self.screen=enemy.screen
        self.width=enemy.screen_width
        self.height=enemy.screen_height
        self.timing=enemy.settings["timing"]
        self.step=enemy.settings["step"]
        self.settings=enemy.settings
        self.bullets=list()
        self.x=enemy.x
        self.y=enemy.y
        self.angle=90
        self.enemy=enemy
    def add(self,x,y,angle):
        bullet=Bullet3(self,x,y,angle)
        self.bullets+=[bullet]
    def update(self):
        if self.gamestate.count%self.timing==0 and self.enemy.life>0:
            self.add(self.x,self.y,self.angle)
            self.angle+=31
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
            if bullet.flag:
                self.bullets.remove(bullet)
                self.add(bullet.x,bullet.y,bullet.angle-self.step)
                self.add(bullet.x,bullet.y,bullet.angle+self.step)
                continue
            bullet.update()
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
class Bullet3:
    def __init__(self,battery,x,y,angle):
        self.gamestate=battery.gamestate
        self.screen=battery.screen
        self.size1=battery.settings["size1"]
        self.size2=battery.settings["size2"]
        self.color=battery.settings["color"]
        self.speed=battery.settings["speed"]
        self.vx=cos(radians(angle))*self.speed
        self.vy=sin(radians(angle))*self.speed
        self.angle=angle
        self.x=x
        self.y=y
        self.pos=list()
        self.update_pos()
        self.count=battery.gamestate.count
        self.flag=False #Trueになったら分裂する
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
        if self.count!=-1 and self.gamestate.count-self.count>80:
            self.flag=True
    def draw(self):
        pygame.draw.polygon(self.screen,self.color,self.pos)

class Battery4:
    def __init__(self,enemy):
        self.gamestate=enemy.gamestate
        self.screen=enemy.screen
        self.width=enemy.screen_width
        self.height=enemy.screen_height
        self.settings=enemy.settings
        self.enemy=enemy
        self.player=enemy.player
        self.bullets=list()
        self.angle=0
    def add(self):
        x=self.enemy.x
        y=self.enemy.y
        for i in range(0,360,8):
            bullet=Bullet4(self,i+self.angle,x,y)
            self.bullets+=[bullet]
        self.angle+=1.3
        return bullet
    def update(self):
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
class Bullet4:
    def __init__(self,battery,angle,x,y):
        self.screen=battery.screen
        self.size1=battery.settings["size1"]
        self.size2=battery.settings["size2"]
        self.color1=battery.settings["color2"]
        self.color2=battery.settings["color1"]
        self.speed1=battery.settings["speed1"]
        self.speed2=battery.settings["speed2"]
        self.color=self.color1
        self.x=x
        self.y=y
        self.vx=cos(radians(angle))*self.speed1
        self.vy=sin(radians(angle))*self.speed1
        self.angle=angle
        self.update_pos()
        self.flag=False
    def update_pos(self):
        self.pos=[
                (cos(radians(self.angle))*self.size1+self.x,sin(radians(self.angle))*self.size1+self.y),
                (cos(radians(self.angle+90))*self.size2+self.x,sin(radians(self.angle+90))*self.size2+self.y),
                (cos(radians(self.angle+180))*self.size1+self.x,sin(radians(self.angle+180))*self.size1+self.y),
                (cos(radians(self.angle+270))*self.size2+self.x,sin(radians(self.angle+270))*self.size2+self.y)]
    def update(self):
        if self.speed1>0:
            self.vx=cos(radians(self.angle))*self.speed1
            self.vy=sin(radians(self.angle))*self.speed1
            self.x+=self.vx
            self.y+=self.vy
            self.speed1-=1
            self.color=self.color1
        else:
            self.x-=cos(radians(self.angle))*self.speed2
            self.y-=sin(radians(self.angle))*self.speed2
            self.flag=True
            self.color=self.color2
        self.update_pos()
    def draw(self):
        pygame.draw.polygon(self.screen,self.color,self.pos)
