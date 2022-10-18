import pygame
from math import sin,cos,radians

class Battery1:
    def __init__(self,enemy):
        self.screen=enemy.screen
        self.bullets=list()
    def update(self):
        for bullet in self.bullets.copy():
            if bullet.y<self.height:
                bullet.update()
            else:
                self.bullet.remove(bullet)
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

class Bullet1:
    def __init__(self,enemy):
        self.screen=enemy.screen
    def update(self):
        pass
    def draw(self):
        pass
