import pygame
from math import sin,cos,radians

class Battery1:
    def __init__(self,main):
        self.screen=main.screen
        self.width=main.width
        self.height=main.height
        self.size=main.settings.player_bullet1["size"]
        self.color=main.settings.player_bullet1["color"]
        self.speed=main.settings.player_bullet1["speed"]
        self.timing=main.settings.player_bullet1["timing"]
        self.bullets=list()
        self.x=main.player.x
        self.y=main.player.y
        self.power=main.player.power
        self.fire=False
    def add(self):
        if int(self.power)==1:
            bullet=Bullet1(self,self.x,self.y)
            self.bullets+=[bullet]
        elif int(self.power)>=2:
            bullet=Bullet1(self,self.x-self.size*1.5,self.y)
            self.bullets+=[bullet]
            bullet=Bullet1(self,self.x+self.size*1.5,self.y)
            self.bullets+=[bullet]
    def update(self,count,x,y,power):
        self.x=x
        self.y=y
        self.power=power
        if count%self.timing==0 and self.fire:
            self.add()
        for bullet in self.bullets.copy():
            if bullet.y<0:
                self.bullets.remove(bullet)
            else:
                bullet.update()
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
class Bullet1:
    def __init__(self,battery,x,y):
        self.screen=battery.screen
        self.width=battery.width
        self.height=battery.height
        self.size=battery.size
        self.color=battery.color
        self.speed=battery.speed
        self.x=x
        self.y=y
    def update(self):
        self.y-=self.speed
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.size)

class Battery2:
    def __init__(self,main):
        self.screen=main.screen
        self.width=main.width
        self.height=main.height
        self.size=main.settings.player_bullet2["size"]
        self.color=main.settings.player_bullet2["color"]
        self.speed=main.settings.player_bullet2["speed"]
        self.timing=main.settings.player_bullet2["timing"]
        self.bullets=list()
        self.x=main.player.x
        self.y=main.player.y
        self.power=main.player.power
        self.fire=False
        self.enemys=list()
    def add(self):
        bullet=Bullet2(self,self.x,self.y)
        self.bullets+=[bullet]
    def update(self,count,x,y,power):
        self.x=x
        self.y=y
        self.power=power
        if count%self.timing==0 and self.fire:
            self.add()
        for bullet in self.bullets.copy():
            if bullet.y<0:
                self.bullets.remove(bullet)
            else:
                bullet.update()
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
class Bullet2:
    def __init__(self,battery,x,y):
        self.screen=battery.screen
        self.width=battery.width
        self.height=battery.height
        self.size=battery.size
        self.color=battery.color
        self.speed=battery.speed
        self.x=x
        self.y=y
    def update(self):
        self.y+=self.speed
        self.x+=self.speed/5
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.size)
