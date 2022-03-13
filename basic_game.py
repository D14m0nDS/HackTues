import pygame
from tileset_func import Tileset
from tilemap_func import Tilemap
from window_create import Window

pygame.init()

clock = pygame.time.Clock()


window_open = Window()

def play_game():
    t_set = Tileset("./images/tileset.png", (16, 16), (0, 0), 0)
    t_map = Tilemap(t_set, (16, 16))
    t_map.draw_map(window_open.window, -50, 300) 
    
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window_open.window.fill((255,255,255))
        t_map.draw_map(window_open.window, -50, 300) 
        
        pygame.display.flip()

play_game()




