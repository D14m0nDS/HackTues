import pygame 
pygame.init()


class Tilemap:
    def __init__(self, tileset, size=(10, 20), map = map ,rect=None):
        self.size = size
        self.tileset = tileset
        self.map = map

        h, w = self.size
        self.image = pygame.Surface((32*w, 32*h))
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()

    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j*32, i*32))

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'      