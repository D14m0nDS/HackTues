import pygame 
import random
pygame.init()

class Tileset:
    def __init__(self, file, size=(32, 32), margin=1, spacing=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def pallete_swap(self, surf, old_c, new_c):
        img_copy = pygame.Surface(surf.get_size())
        img_copy.fill(new_c)
        surf.set_colorkey(old_c)
        img_copy.blit(surf, (0, 0))
        return img_copy


    def get_rgb_color(self, tuple, delta):
        if all([var <= (255 - delta*2) for var in tuple]):
            tuple = [var + delta for var in tuple]
        return tuple

    def load(self):
        self.tiles = []
        x0, y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing
        
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255) 

        
        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tuple = (a, b, c)

                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (y, x, *self.size))
                tile = self.pallete_swap(tile, (255, 255, 255), (self.get_rgb_color(tuple, 20)))
                tile = self.pallete_swap(tile, (151, 151, 151), (self.get_rgb_color(tuple, 30)))
                tile = self.pallete_swap(tile, (109, 109, 109), (self.get_rgb_color(tuple, 40)))
                tile = self.pallete_swap(tile, (98, 98, 98), (self.get_rgb_color(tuple, 50)))
                tile = self.pallete_swap(tile, (145, 145, 145), (self.get_rgb_color(tuple, 60)))
                tile = self.pallete_swap(tile, (200, 200, 200), (self.get_rgb_color(tuple, 70)))
                tile = self.pallete_swap(tile, (203, 203, 203), (self.get_rgb_color(tuple, 80)))
                tile = self.pallete_swap(tile, (189, 189, 189), (self.get_rgb_color(tuple, 90)))
                tile = self.pallete_swap(tile, (170, 170, 170), (self.get_rgb_color(tuple, 100)))
                tile = self.pallete_swap(tile, (125, 125, 125), (self.get_rgb_color(tuple, 110)))
                tile = self.pallete_swap(tile, (228, 228, 228), (self.get_rgb_color(tuple, 120)))
                tile = self.pallete_swap(tile, (150, 150, 150), (self.get_rgb_color(tuple, 130)))

                
                
                self.tiles.append(tile)

    

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'