import pygame

class Window:
    def __init__(self,):
        self.DISPLAY_W, self.DISPLAY_H = 720, 480
        display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))