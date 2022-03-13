import pygame
import pygame.locals
from world_generation import map
TILE_SIZE = 16

map = map()

class Tilemap():
    def __init__(self, tileset, tile_size = TILE_SIZE):
        print()
        self.tileset = tileset
        # self.width, self.height = size
        self.tile_size = TILE_SIZE

    # def draw_map(self, tileset):
    #     self.tileset[0]

    def draw_map(self, screen):
        self.MAP_HEIGHT = len(map.map[0]) 
        self.MAP_WIDTH = len(map.map)
        for row in range(self.MAP_WIDTH):
            for col in range(self.MAP_HEIGHT):
                
                # print(f'row = {row}')
                # print(f'col = {col}')
                # print(f'map = {map.map[row][col]}')
                # print(f'tiles = {self.tileset.tiles}')
                # print(f'pp big = {row*self.MAP_HEIGHT + col}')
                screen.blit(self.tileset.tiles[map.map[row][col]], (row*TILE_SIZE, col*TILE_SIZE))  


    # def create_texture(self):
    #     self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
    #     self.image.fill(map.materials)
    #     return self.image

    # def generate_map(self, tile_size = TILE_SIZE):
    #     self.map_data = map.map
    #     for i in range(self.height // tile_size):
    #         self.map_data.append([])
    #         for j in range(self.width // tile_size):
    #             if map.materials == 
    #             tile = self.tileset.tiles[self.map[i, j]]
    #             # convert to hex from string value
    #             self.tile = int(hex(self.tiles[self.rand_index]), 16)
    #             self.map_data[i].append(self.tile)
    #     return self.map_data

   


    # def load_tile_table(filename, width, height):
    #     image = pygame.image.load(filename).convert()
    #     image_width, image_height = image.get_size()
    #     tile_table = []
    #     for tile_x in range(0, image_width/width):
    #         line = []
    #         tile_table.append(line)
    #         for tile_y in range(0, image_height/height):
    #             rect = (tile_x*width, tile_y*height, width, height)
    #             line.append(image.subsurface(rect))
    #     return tile_table

    # if __name__=='__main__':
    #     pygame.init()
    #     screen = pygame.display.set_mode((128, 98))
    #     screen.fill((255, 255, 255))
    #     table = load_tile_table("tileset.png", 24, 16)
    #     for x, row in enumerate(table):
    #         for y, tile in enumerate(row):
    #             screen.blit(tile, (x*32, y*24))
    #     pygame.display.flip()
    #     while pygame.event.wait().type != pygame.locals.QUIT:   
    #         pass