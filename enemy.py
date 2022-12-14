import pygame
from random import randint
from math import sin,cos,radians
from enemy_bullet import Battery1,Battery2,Battery3,Battery4,Battery5
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
        self.height1=main.settings.enemy1["height1"]
        self.height2=main.settings.enemy1["height2"]
        self.max_enemys=main.settings.enemy1["max_enemys"]
        self.player_size=main.player.coll
        self.items=main.items
        self.flag=False
        self.enemys=list()
        self.enemys_count=0
    def add(self):
        x=0
        y=self.height
        enemy=Enemy1(self,x,y,0)
        self.enemys+=[enemy]
    def update(self,count,x,y):
        if self.enemys_count<self.max_enemys:
            if count%self.timing==0:
                self.enemys_count+=1
                self.add()
        else:
            self.gamestate.gameflag="empty"
        for enemy in self.enemys.copy():
            if True in [(0<=x<=self.screen_width and 0<=y<=self.screen_height) for x,y in enemy.pos]:
                enemy.update(count,x,y)
            else:
                self.enemys.remove(enemy)
        if self.flag:
            self.height+=5
            if self.height>self.height2:
                self.flag=False
        else:
            self.height-=5
            if self.height<self.height1:
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

class Enemy2:
    def __init__(self,main):
        self.gamestate=main.gamestate
        self.screen=main.screen
        self.screen_width=main.width
        self.screen_height=main.height
        self.size1=main.settings.enemy2["size1"]
        self.size2=main.settings.enemy2["size2"]
        self.color1=main.settings.enemy2["color1"]
        self.color2=main.settings.enemy2["color2"]
        self.points=main.settings.enemy2["points"]
        self.pos1=main.settings.enemy2["pos1"]
        self.pos2=main.settings.enemy2["pos2"]
        self.settings=main.settings.enemy_bullet2
        self.rect1_1=pygame.Rect((0,0,self.size1*2,self.size1*2))
        self.rect1_1.center=self.pos1
        self.rect1_2=pygame.Rect((0,0,self.size2*2,self.size2*2))
        self.rect1_2.center=self.pos1
        self.rect2_1=pygame.Rect((0,0,self.size1*2,self.size1*2))
        self.rect2_1.center=self.pos2
        self.rect2_2=pygame.Rect((0,0,self.size2*2,self.size2*2))
        self.rect2_2.center=self.pos2
        self.player=main.player
        self.battery=Battery1(self)
        self.life=[main.settings.enemy2["life"]]*2
        self.old_life=self.life.copy()
        self.items=main.items
        self.items.prob=100
    def update(self):
        if self.old_life[0]>0 and self.life[0]<=0:
            for i in range(10):
                x=self.pos1[0]+randint(-self.size1,self.size1)
                y=self.pos1[1]+randint(-self.size1,self.size1)
                self.items.add(x,y)
            self.gamestate.score+=self.points
            self.battery.bullets=[]
        if self.old_life[1]>0 and self.life[1]<=0:
            for i in range(10):
                x=self.pos2[0]+randint(-self.size1,self.size1)
                y=self.pos2[1]+randint(-self.size1,self.size1)
                self.items.add(x,y)
            self.gamestate.score+=self.points
        if self.gamestate.gameflag=="playing" and self.life[0]<=0 and self.life[1]<=0:
            self.gamestate.gameflag="empty"
        self.items.update()
        self.battery.update()
        self.old_life=self.life.copy()
    def draw(self):
        self.items.draw()
        self.battery.draw()
        if self.life[0]>0:
            pygame.draw.rect(self.screen,self.color1,self.rect1_1)
            pygame.draw.rect(self.screen,self.color2,self.rect1_2)
        if self.life[1]>0:
            pygame.draw.rect(self.screen,self.color1,self.rect2_1)
            pygame.draw.rect(self.screen,self.color2,self.rect2_2)
class Enemy3:
    def __init__(self,main):
        self.gamestate=main.gamestate
        self.player=main.player
        self.screen=main.screen
        self.screen_width=main.width
        self.screen_height=main.height
        self.amount=main.settings.enemy3["amount"]
        self.size1=main.settings.enemy3["size1"]
        self.size2=main.settings.enemy3["size2"]
        self.color1=main.settings.enemy3["color1"]
        self.color2=main.settings.enemy3["color2"]
        self.points=main.settings.enemy3["points"]
        self.speed=main.settings.enemy3["speed"]
        self.settings=main.settings.enemy_bullet3
        self.circle_size=main.settings.enemy3["circle_size"]
        self.enemys_pos=[(cos(radians(i))*self.circle_size+self.screen_width/2,
            sin(radians(i))*self.circle_size+self.screen_width/2) for i in range(0,360,int(360/self.amount))]
        self.enemys_life=[main.settings.enemy3["life"]]*self.amount
        self.old_life=self.enemys_life.copy()
        self.items=main.items
        self.angle=0
        self.battery=Battery2(self)
    def update(self):
        for i in range(self.amount):
            if self.old_life[i]>0 and self.enemys_life[i]<=0:
                for j in range(10):
                    x=self.enemys_pos[i][0]+randint(-self.size1,self.size1)
                    y=self.enemys_pos[i][1]+randint(-self.size1,self.size1)
                    self.items.add(x,y)
                self.gamestate.score+=self.points
                self.battery.bullets=[]
        if [True for i in self.enemys_life if i<=0]==[True]*self.amount:
            self.gamestate.gameflag="empty"
        self.items.update()
        self.enemys_pos=[(cos(radians(i+self.angle))*self.circle_size+self.screen_width/2,
    sin(radians(i+self.angle))*self.circle_size+self.screen_width/2) for i in range(0,360,int(360/self.amount))]
        self.angle+=self.speed
        self.battery.update()
        self.old_life=self.enemys_life.copy()
    def draw(self):
        self.battery.draw()
        self.items.draw()
        for i in range(self.amount):
            if self.enemys_life[i]>0:
                pygame.draw.circle(self.screen,self.color1,self.enemys_pos[i],self.size1)
                pygame.draw.circle(self.screen,self.color2,self.enemys_pos[i],self.size2)

class Enemy4:
    def __init__(self,main):
        self.gamestate=main.gamestate
        self.player=main.player
        self.screen=main.screen
        self.screen_width=main.width
        self.screen_height=main.height
        self.size1=main.settings.enemy4["size1"]
        self.size2=main.settings.enemy4["size2"]
        self.color1=main.settings.enemy4["color1"]
        self.color2=main.settings.enemy4["color2"]
        self.points=main.settings.enemy4["points"]
        self.life=main.settings.enemy4["life"]
        self.settings=main.settings.enemy_bullet4
        self.x=self.screen_width/2
        self.y=self.screen_width/3
        self.pos=[(cos(radians(i+90))*self.size1+self.x,sin(radians(i+90))*self.size1+self.y)
                for i in range(0,360,60)]
        self.pos2=[(cos(radians(i+90))*self.size2+self.x,sin(radians(i+90))*self.size2+self.y)
                for i in range(0,360,60)]
        self.battery=Battery3(self)
        self.items=main.items
    def update(self):
        if self.life<=0 and self.gamestate.gameflag=="playing":
            self.gamestate.gameflag="empty"
            for i in range(15):
                x=self.x+randint(-self.size1,self.size1)*2
                y=self.y+randint(-self.size1,self.size1)*2
                self.items.add(x,y)
            self.gamestate.score+=self.points
            self.battery.bullets=[]
        self.items.update()
        self.battery.update()
    def draw(self):
        self.battery.draw()
        self.items.draw()
        if self.life>0:
            pygame.draw.polygon(self.screen,self.color1,self.pos)
            pygame.draw.polygon(self.screen,self.color2,self.pos2)

class Enemy5:
    def __init__(self,main):
        self.gamestate=main.gamestate
        self.player=main.player
        self.screen=main.screen
        self.screen_width=main.width
        self.screen_height=main.height
        self.size=main.settings.enemy5["size"]
        self.color=main.settings.enemy5["color"]
        self.speed=main.settings.enemy5["speed"]
        self.points=main.settings.enemy5["points"]
        self.move_dis=main.settings.enemy5["move_dis"]
        self.life=main.settings.enemy5["life"]
        self.move_now=self.move_dis
        self.angle=135
        self.vx=cos(radians(self.angle))*self.speed
        self.vy=sin(radians(self.angle))*self.speed
        self.x=self.screen_width/2
        self.y=main.settings.enemy5["y"]
        self.settings=main.settings.enemy_bullet5
        self.update_pos()
        self.battery=Battery4(self)
        self.bullet=None
        self.items=main.items
    def update_pos(self):
        self.pos1=[(cos(radians(i+90))*self.size+self.x,sin(radians(i+90))*self.size+self.y)
                for i in range(0,360,120)]
        self.pos2=[(cos(radians(i-90))*self.size+self.x,sin(radians(i-90))*self.size+self.y)
                for i in range(0,360,120)]
    def update(self):
        if self.life<=0:
            if self.gamestate.gameflag=="playing":
                self.gamestate.gameflag="empty"
                for i in range(20):
                    x=self.x+randint(-self.size,self.size)
                    y=self.y+randint(-self.size,self.size)
                    self.items.add(x,y)
                self.gamestate.score+=self.points
                self.battery.bullets=[]
        elif self.battery.bullets==[] or ((not self.bullet is None) and (self.bullet.flag)):
            self.x+=self.vx
            self.y+=self.vy
            self.move_now-=self.speed
            if self.move_now<=0:
                self.move_now=self.move_dis
                self.angle-=90
                self.vx=cos(radians(self.angle))*self.speed
                self.vy=sin(radians(self.angle))*self.speed
                self.bullet=self.battery.add()
            self.update_pos()
        self.items.update()
        self.battery.update()
    def draw(self):
        self.battery.draw()
        self.items.draw()
        if self.life>0:
            pygame.draw.polygon(self.screen,self.color,self.pos1)
            pygame.draw.polygon(self.screen,self.color,self.pos2)
class Enemy6:
    def __init__(self,main):
        self.screen=main.screen
        self.player=main.player
        self.gamestate=main.gamestate
        self.items=main.items
        self.width=main.width
        self.height=main.height
        self.size=main.settings.enemy6["size"]
        self.color=main.settings.enemy6["color"]
        self.points=main.settings.enemy6["points"]
        self.life=main.settings.enemy6["life"]
        self.timing=main.settings.enemy6["timing"]
        self.settings=main.settings.enemy_bullet6
        self.x=self.width/2
        self.y=self.width/4
        self.battery=Battery5(self)
    def update(self):
        if self.life<=0:
            if self.gamestate.gameflag=="playing":
                self.gamestate.gameflag="empty"
                self.battery.bullets=[]
                for i in range(20):
                    x=self.x+randint(-self.size,self.size)
                    y=self.y+randint(-self.size,self.size)
                    self.items.add(x,y)
                self.gamestate.score+=self.points
        if self.gamestate.count%self.timing==0 and self.gamestate.gameflag=="playing":
            self.battery.add()
        self.items.update()
        self.battery.update()
    def draw(self):
        self.battery.draw()
        if self.life>0:
            pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.size)
        self.items.draw()
