import pygame as pg
from world_generation import map
from tileset_func import Tileset
from tilemap_func import Tilemap

gen = map()

t_set = Tileset("./images/tileset.png", (16, 16), 0, 0)
t_map = Tilemap(t_set, (gen.w, gen.h), gen.map)

t_map.render()
