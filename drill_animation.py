import pygame as pg, sys
import os
import time

from pygame.locals import *

# Constants
clock = pg.time.Clock()

class Drill(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pg.image.load('Drill1.png'))
        self.sprites.append(pg.image.load('Drill2.png'))
        self.sprites.append(pg.image.load('Drill3.png'))
        self.sprites.append(pg.image.load('Drill4.png'))
        self.sprites.append(pg.image.load('Drill5.png'))
        self.sprites.append(pg.image.load('Drill6.png'))
        self.sprites.append(pg.image.load('Drill7.png'))
        self.sprites.append(pg.image.load('Drill8.png'))
        self.sprites.append(pg.image.load('Drill9.png'))
        self.sprites.append(pg.image.load('Drill10.png'))
        self.sprites.append(pg.image.load('Drill11.png'))
        self.current_sprite_index = 0
        self.image = self.sprites[self.current_sprite_index]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite_index += 1
        print('heh')
        if self.current_sprite_index >= 11:
            self.current_sprite_index = 0
        self.image = self.sprites[int(self.current_sprite_index)]


screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Sprite Animation")


moving_sprites = pg.sprite.Group()
drill = Drill(420, 300)
moving_sprites.add(drill)

pg.display.set_caption("BDSM")
icon = pg.image.load("space-station.png")
pg.display.set_icon(icon)

running = True

while running:

    pg.init()
    for event in pg.event.get():
         if event.type == quit:
              running = False
              pg.quit()
              break

    # Drawing and updating
    moving_sprites.draw(screen)
    moving_sprites.update()

    # Update the contents of the entire display
    pg.display.update()
    pg.display.flip()
