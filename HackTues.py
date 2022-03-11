import pygame as pg
import os
import random

pg.init()

WIDTH, HEIGHT = 800, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT)) #create window
pg.display.set_caption("SHTO NE TRUGWA") #set display caption

def planet_creator():
    width_planet = random.randint(400, 800)
    height_planet = random.randint(250, 500)
    PLANET = pg.image.load(os.path.join('images', 'planet.jpg'))
    PLANET_RESIZE = pg.transform.scale(PLANET, (width_planet, height_planet))
    WIN.blit(PLANET_RESIZE, (400, 250))

def main():

    #closing the window
    run = True 
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
    
        #WIN.fill((255,255,255))
        pg.display.update()
        BACKGROUND = pg.image.load(os.path.join('images', 'space.jpg'))
        BACKGROUND_RESIZE = pg.transform.scale(BACKGROUND, (800, 500))
        WIN.blit(BACKGROUND_RESIZE, (0, 0))

        #tuka shte se chekwa dali sa stignati neobhodimite resursi za da se otide na/naprawi nowa planeta 
        planet_creator()
        pg.display.update()
        
    pg.quit()


main()