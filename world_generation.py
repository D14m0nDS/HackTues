import pygame as pg
from  world_building import *

planet = Planet_return_type()

class map:
    def __init__(self):
        self.map = planet.planet_array
        self.planet_settings = planet.Planet
        self.planet_size = (planet.Planet.width, planet.Planet.height)
        self.materials = planet.materials
        self.materials_count = planet.materials_count
        print(f'size planet = {self.planet_size}')
        print(f'array planet = {planet.planet_array}')

