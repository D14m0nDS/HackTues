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
                # tile = self.pallete_swap(tile, (255, 255, 255), ()))
                # tile = self.pallete_swap(tile, (151, 151, 151), ()))
                # tile = self.pallete_swap(tile, (109, 109, 109), ()))
                # tile = self.pallete_swap(tile, (98, 98, 98), ()))
                # tile = self.pallete_swap(tile, (145, 145, 145), ()))
                # tile = self.pallete_swap(tile, (200, 200, 200), ()))
                # tile = self.pallete_swap(tile, (203, 203, 203), ()))
                # tile = self.pallete_swap(tile, (189, 189, 189), ()))
                # tile = self.pallete_swap(tile, (170, 170, 170), ()))
                # tile = self.pallete_swap(tile, (125, 125, 125), ()))
                # tile = self.pallete_swap(tile, (228, 228, 228), ()))
                # tile = self.pallete_swap(tile, (150, 150, 150), ()))

                tile = self.pallete_swap(tile, (255, 255, 255), (83, 73, 191))
                tile = self.pallete_swap(tile, (151, 151, 151), (55, 48, 128))
                tile = self.pallete_swap(tile, (109, 109, 109), (110, 96, 255))
                tile = self.pallete_swap(tile, (98, 98, 98), (28, 24, 64))
                tile = self.pallete_swap(tile, (145, 145, 145), (99, 87, 230))
                tile = self.pallete_swap(tile, (200, 200, 200), (73, 100, 191))
                tile = self.pallete_swap(tile, (203, 203, 203), (48, 67, 128))
                tile = self.pallete_swap(tile, (189, 189, 189), (96, 134, 255))
                tile = self.pallete_swap(tile, (170, 170, 170), (24, 33, 64))
                tile = self.pallete_swap(tile, (125, 125, 125), (87, 120, 230))
                tile = self.pallete_swap(tile, (228, 228, 228), (38, 92, 255))
                tile = self.pallete_swap(tile, (150, 150, 150), (118, 84, 255))

                
                
                self.tiles.append(tile)

    

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'