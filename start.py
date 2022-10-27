import pygame
import sys
from stage import Stage
from stage1 import Stage1
from stage2 import Stage2
from stage3 import Stage3
from stage4 import Stage4
from stage5 import Stage5
from ending import Ending

class Start(Stage):
    def __init__(self,main):
        super().__init__(main)
        pygame.font.init()
        self.font=pygame.font.SysFont(None,50)
        self.num=0
        self.stages=[Stage1,Stage2,Stage3,Stage4,Stage5]
        self.stages_amount=len(self.stages)
        self.names=["Start","Stage1","Stage2","Stage3","Stage4","Stage5"]
        self.main=main
        self.start_texts=list()
        self.start_rects=list()
        for i in range(self.stages_amount+1):
            color=(255,0,0) if i==0 else (255,255,255)
            self.start_texts+=[self.font.render(self.names[i],True,color,self.bg_color)]
            self.start_rects+=[self.start_texts[i].get_rect()]
            self.start_rects[i].center=(self.width/2,self.height/2)
            if i!=0:
                self.start_rects[i].top=self.start_rects[i-1].bottom+50
    def nextstage(self,stage):
        yield stage
        yield Ending
    def keydown(self,key):
        if key==pygame.K_ESCAPE:
            sys.exit()
        elif key==pygame.K_RETURN:
            if self.num!=0:
                self.main.stages=self.nextstage(self.stages[self.num-1])
            self.gamestate.gameflag="nextstage"
        elif key==pygame.K_DOWN:
            self.num+=1
            if self.num>self.stages_amount:
                self.num-=1
            else:
                for i in self.start_rects:
                    i.y-=36+50
            for i in range(self.stages_amount+1):
                if i==self.num:
                    rect=self.start_rects[i]
                    self.start_texts[i]=self.font.render(self.names[i],True,(255,0,0),self.bg_color)
                    self.start_rects[i]=rect
                else:
                    rect=self.start_rects[i]
                    self.start_texts[i]=self.font.render(self.names[i],True,(255,255,255),self.bg_color)
                    self.start_rects[i]=rect
        elif key==pygame.K_UP:
            self.num-=1
            if self.num<0:
                self.num+=1
            else:
                for i in self.start_rects:
                    i.y+=36+50
            for i in range(self.stages_amount+1):
                if i==self.num:
                    rect=self.start_rects[i]
                    self.start_texts[i]=self.font.render(self.names[i],True,(255,0,0),self.bg_color)
                    self.start_rects[i]=rect
                else:
                    rect=self.start_rects[i]
                    self.start_texts[i]=self.font.render(self.names[i],True,(255,255,255),self.bg_color)
                    self.start_rects[i]=rect
    def keyup(self,key):
        pass
    def draw(self):
        for i in range(self.stages_amount+1):
            self.screen.blit(self.start_texts[i],self.start_rects[i])
