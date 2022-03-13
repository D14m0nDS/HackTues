import pygame as pg, sys

mainClock = pg.time.Clock()

from pygame.locals import *
pg.init()

screen = pg.display.set_mode((800, 600),0,32)
background = pg.image.load("background1.png")

pg.display.set_caption("BDSM")
icon = pg.image.load("planet-earth.png")
pg.display.set_icon(icon)

planetImg = pg.image.load("planet-earth (4).png")
angle = 0

running = True

while running:
    pg.time.delay(50)

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    x = 395
    y = 700
    vel = 5

    img_copy = pg.transform.rotate(planetImg, angle)
    screen.blit(img_copy, (x - int(img_copy.get_width()/2),y - int(img_copy.get_height() / 2)))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            angle -= vel
        if event.key == pg.K_RIGHT:
            angle += vel
            img_copy = pg.transform.rotate(planetImg, angle)

    pg.time.delay(100)
    pg.display.update()

pg.quit()
