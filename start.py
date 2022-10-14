import pygame
import sys
from stage import Stage

class Start(Stage):
    def __init__(self,main):
        super().__init__(main)
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
    def keyup(self,key):
        pass
