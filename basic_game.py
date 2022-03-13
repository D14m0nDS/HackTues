import pygame as pg
from walking_animation import *
from tileset_func import Tileset
from tilemap_func import Tilemap
from window_create import Window

clock = pg.time.Clock()

p = Player

# p.walking_left(p)
# p.walking_right(p)
# p.doing_task(p)
# p.standing_still(p)
# p.update(p)

moving_sprites = pg.sprite.Group()
player = p(420, 300)
moving_sprites.add(player)

window_open = Window()

def play_game():
    t_set = Tileset("./images/tileset.png", (16, 16), (0, 0), 0)
    t_map = Tilemap(t_set, (16, 16))
    t_map.draw_map(window_open.window, -50, 300)
    
    running = True
    while running:
        pg.init()
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        keys = pg.key.get_pressed()
        x = 400
        y = 370
        vel = 5
        window_open.window.fill((255,255,255))
        screen.blit(background, (0, 0))
        
        

        
        t_map.draw_map(window_open.window, -50, 350) 

        # Initialisin


        # Working with keys
        # for p.event in pg.event.get():
        #  if event.type == quit:
        #       running = False
        #       pg.quit()
        #       break
        #  if p.event.type == pg.KEYDOWN:
        #      if event.key == pg.K_LEFT:
        #         p.angle-=vel
        #         p.img_copy = pg.transform.rotate(background, angle)
        #         p.player.walking_left()
        #      elif p.event.key == pg.K_RIGHT:
        #          p.angle+=vel
        #          p.player.walking_right()
        #      elif p.event.key == pg.K_UP:
        #          p.player.doing_task()
        #  else:
        #      p.player.standing_still()
        # Drawing

        # img_copy = pg.transform.rotate(background, angle)
        # screen.blit(img_copy, (x - int(img_copy.get_width() / 2), y - int(img_copy.get_height() / 2)))

        # Drawing and updating
        moving_sprites.draw(screen)
        moving_sprites.update()

        # Update the contents of the entire display
        pg.display.update()
        pg.display.flip()

play_game()