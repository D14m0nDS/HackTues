import pygame
from world_generation import map
from tileset_func import Tileset
from tilemap_func import Tilemap
from window_create import Window

gen = map()
t_set = Tileset
t_map = Tilemap

winwod_open = Window()

def play_menu():
    t_set = Tileset("./images/tileset.png", (16, 16), 0, 0)
    t_map = Tilemap(t_set, gen.width, gen.height, gen.map)
    t_map.render() 


