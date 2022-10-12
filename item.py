import pygame
from random import randint
from math import *
from functions import *

class Items1:
    def __init__(self,firinghole,settings,player):
        self.player=player
        self.screen=firinghole.screen
        self.height=firinghole.screen_height
        self.settings=settings
        self.prob=settings["prob"]
        self.speed=settings["speed3"]
        self.items=list()
    def add(self,x,y):
        if randint(0,100)<=self.prob:
            item=Item1(self,x,y)
            self.items+=[item]
    def update(self):
        x1=self.player.x
        y1=self.player.y
        for item in self.items.copy():
            if item.y>self.height:
                self.items.remove(item)
                continue
            x2=item.x
            y2=item.y
            if item.flag:
                angle=atan2(y1-y2,x1-x2)
                item.x+=cos(angle)*self.speed
                item.y+=sin(angle)*self.speed
                if distance(x1,y1,item.x,item.y)<=self.player.size:
                    self.player.power+=item.power
                    self.items.remove(item)
                continue
            if distance(x1,y1,x2,y2)<=self.player.item_coll:
                item.flag=True
                continue
            item.update()
    def draw(self):
        for item in self.items:
            item.draw()
class Item1:
    def __init__(self,items,x,y):
        self.screen=items.screen
        self.size1=items.settings["size1"]
        self.size2=items.settings["size2"]
        self.color1=items.settings["color1"]
        self.color2=items.settings["color2"]
        self.speed1=items.settings["speed1"]
        self.speed2=items.settings["speed2"]
        self.speed=randint(self.speed1*10,self.speed2*10)/10
        self.power=items.settings["power"]
        self.flag=False
        self.x=x
        self.y=y
    def update(self):
        self.y+=self.speed
    def draw(self):
        pygame.draw.circle(self.screen,self.color1,(self.x,self.y),self.size1)
        pygame.draw.circle(self.screen,self.color2,(self.x,self.y),self.size2)
