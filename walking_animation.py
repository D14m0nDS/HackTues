import pygame as pg, sys

from pygame.locals import *

#Base station sprite
class Base(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pg.image.load('Base.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

#Player sprite
class Player(pg.sprite.Sprite):
   def __init__(self, pos_x, pos_y):
       super().__init__()
       self.sprites = []
       self.walking_left_animation = False
       self.walking_right_animation = False
       self.doing_task_animation = False
       self.sprites.append(pg.image.load('Walking_left_1.png'))
       self.sprites.append(pg.image.load('Walking_left_2.png'))
       self.sprites.append(pg.image.load('Walking_left_3.png'))
       self.sprites.append(pg.image.load('Walking_left_4.png'))
       self.sprites.append(pg.image.load('Walking_left_5.png'))
       self.sprites.append(pg.image.load('Walking_left_6.png'))
       self.sprites.append(pg.image.load('Walking_right_1.png'))
       self.sprites.append(pg.image.load('Walking_right_2.png'))
       self.sprites.append(pg.image.load('Walking_right_3.png'))
       self.sprites.append(pg.image.load('Walking_right_4.png'))
       self.sprites.append(pg.image.load('Walking_right_5.png'))
       self.sprites.append(pg.image.load('Walking_right_6.png'))
       self.sprites.append(pg.image.load('Standing2.png'))
       self.sprites.append(pg.image.load('Standing3.png'))
       self.sprites.append(pg.image.load('Standing4.png'))
       self.sprites.append(pg.image.load('Standing5.png'))
       self.sprites.append(pg.image.load('Standing6.png'))
       self.sprites.append(pg.image.load('Standing.png'))
       self.current_sprite_index = 0
       self.image = self.sprites[self.current_sprite_index]

       self.rect = self.image.get_rect()
       self.rect.topleft = [pos_x, pos_y]

   # Confirming left key being pressed
   def walking_left(self):
       self.walking_left_animation = True
       self.walking_right_animation = False
       self.doing_task_animation = False
       print('walking left')

   # Confirming right key being pressed
   def walking_right(self):
       self.walking_right_animation = True
       self.walking_left_animation = False
       self.doing_task_animation = False
       print('walking right')

   # Confirm doing a task
   def doing_task(self):
       self.doing_task_animation = True
       self.walking_right_animation = False
       self.walking_left_animation = False
       print('doing task')

   # Confirm doing nothing
   def standing_still(self):
       self.walking_left_animation = False
       self.walking_right_animation = False
       self.doing_task_animation = False

   # Animating player
   def update(self):
       angle = 0
       vel = 5
       if self.walking_left_animation == True:
           self.current_sprite_index += 1
           if self.current_sprite_index >= 6:
                self.current_sprite_index = 0
       elif self.walking_right_animation == True:
           self.current_sprite_index += 1
           if self.current_sprite_index >= 12:
                self.current_sprite_index = 6
       elif self.doing_task_animation == True:
           self.current_sprite_index +=1
           if self.current_sprite_index >= 17:
               self.current_sprite_index = 12
       else:
            self.current_sprite_index = 17
       print(self.current_sprite_index)
       self.image = self.sprites[int(self.current_sprite_index)]

#General setup
clock = pg.time.Clock()

screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Sprite Animation")
background = pg.image.load("background.png")

angle = 0
vel = 5

# Creating the sprites and groups
moving_sprites = pg.sprite.Group()
player = Player(420, 300)
moving_sprites.add(player)

static_sprites = pg.sprite.Group()
base = Base(200, 210)
static_sprites.add(base)

#Display setup
pg.display.set_caption("BDSM")
# icon = pg.image.load("space-station.png")
# pg.display.set_icon(icon)
background_image = pg.image.load("background.png")

running = True

# Game loop
# while running:
#     # Initialising
#     pg.init()

#     screen.fill((255, 255, 255))
#     screen.blit(background, (0, 0))

#     pg.time.delay(50)

#     keys = pg.key.get_pressed()
#     x = 400
#     y = 370
#     vel = 5


#     img_copy = pg.transform.rotate(background, angle)
#     screen.blit(img_copy, (x - int(img_copy.get_width() / 2), y - int(img_copy.get_height() / 2)))

#     # Working with keys
#     for event in pg.event.get():
#          if event.type == quit:
#               running = False
#               pg.quit()
#               break
#          if event.type == pg.KEYDOWN:
#              if event.key == pg.K_LEFT:
#                  angle-=vel
#                  img_copy = pg.transform.rotate(background, angle)
#                  player.walking_left()
#              elif event.key == pg.K_RIGHT:
#                  angle+=vel
#                  player.walking_right()
#              elif event.key == pg.K_UP:
#                  player.doing_task()
#          else:
#              player.standing_still()
#     # Drawing

#     img_copy = pg.transform.rotate(background, angle)
#     # Drawing and updating
#     moving_sprites.draw(screen)
#     static_sprites.draw(screen)
#     moving_sprites.update()

#     # Update the contents of the entire display
#     pg.display.update()
#     pg.display.flip()
#     clock.tick(60)