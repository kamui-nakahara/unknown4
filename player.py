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
        self.speed=main.settings.player["speed"]
        self.slow=main.settings.player["slow"]
        self.power=main.settings.player["power"]
        self.max_power=main.settings.player["max_power"]
        self.item_coll=main.settings.player["item_coll"]
        self.life=main.settings.player["life"]
        self.move_up=False
        self.move_down=False
        self.move_left=False
        self.move_right=False
        self.move_slow=False
    def update(self):
        if self.move_slow:
            speed=self.slow
        else:
            speed=self.speed
        if self.move_up and self.y-speed-self.size>=0:self.y-=speed
        if self.move_down and self.y+speed+self.size<=self.height:self.y+=speed
        if self.move_left and self.x-speed-self.size>=0:self.x-=speed
        if self.move_right and self.x+speed+self.size<=self.width:self.x+=speed
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.size)
        pygame.draw.circle(self.screen,self.coll_color,(self.x,self.y),self.coll)
