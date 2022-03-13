import pygame

class Window:
    def __init__(self,):
        self.DISPLAY_W, self.DISPLAY_H = 720, 480
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))