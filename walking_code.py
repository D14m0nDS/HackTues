import pygame 
pygame.init()

window = pygame.display.setImode((400, 400))
pygame.display.set_caption("Movement Trail Base:")

x = 40
# y - 40
width = 30
height = 100
vel = 5

from pygame.locals import(
    K_A,
    K_D,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


walk  = True

while walk:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == QUIT:
            walk = False

