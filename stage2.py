import pygame
from stage import Stage

class Stage2(Stage):
    def __init__(self,main):
        super().__init__(main)
    def update(self):
        self.player.update()
        self.battery1.update(self.gamestate.count,self.player.x,self.player.y,self.player.power)
    def draw(self):
        self.battery1.draw()
        self.player.draw()
