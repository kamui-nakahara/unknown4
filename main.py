import pygame
import sys
from math import *
from settings import Settings
from player import Player
from bullet import Battery1
from enemy import FiringHole

class Main:
    def __init__(self):
        self.settings=Settings()
        self.width=self.settings.display["width"]
        self.height=self.settings.display["height"]
        self.bg_color=self.settings.display["bg_color"]
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.player=Player(self)
        self.battery1=Battery1(self)
        self.firinghole=FiringHole(self)
        self.pause=False
        self.count=0
    def loop(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self.keydown(event.key)
            elif event.type==pygame.KEYUP:
                self.keyup(event.key)
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
        elif key==pygame.K_RETURN:
            self.pause=not self.pause
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
        if not self.pause:
            self.player.update()
            self.battery1.update(self.count,self.player.x,self.player.y,self.player.power)
            self.firinghole.update(self.count)
            for bullet in self.battery1.bullets.copy():
                x=bullet.x
                y=bullet.y
                for enemy in self.firinghole.enemys.copy():
                    pos=enemy.pos
                    for [x1,y1],[x2,y2] in zip(pos,pos[1:]+[pos[0]]):
                        a=atan2(y2-y1,x2-x1)
                        b=atan2(y-y1,x-x1)
                        c=a-b
                        d=((x1-x)**2+(y1-y)**2)**0.5
                        e=sin(c)*d
                        f=cos(c)*d
                        g=cos(a)*f+x1
                        h=sin(a)*f+y1
                        if abs(e)<=bullet.size and \
                                (x1<=g<=x2 or x2<=g<=x1) and (y1<=h<=y2 or y2<=h<=y1):
                            if enemy in self.firinghole.enemys:
                                self.firinghole.enemys.remove(enemy)
                            if bullet in self.battery1.bullets:
                                self.battery1.bullets.remove(bullet)
        self.count+=1
    def draw(self):
        self.screen.fill(self.bg_color)
        self.battery1.draw()
        self.player.draw()
        self.firinghole.draw()
        pygame.display.update()
if __name__=="__main__":
    main=Main()
    main.loop()
