import pygame

class Player:
    def __init__(self,main):
        self.screen=main.screen
        self.width=main.width
        self.height=main.height
        self.coll=main.settings.player["coll_size"]
        self.x=main.settings.player["x"]
        self.y=main.settings.player["y"]
        self.size=main.settings.player["size"]
        self.color=main.settings.player["color"]
        self.coll_color=main.settings.player["coll_color"]
    def update(self):
        pass
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.size
