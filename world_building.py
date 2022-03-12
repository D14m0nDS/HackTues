import pygame as pg
import os
import random
import time

class Planet:
    def __init__(self):
        self.width = random.randint(20, 21)
        self.height = 5
        self.gravity = random.randint(0, 100)
        self.air_pressure = random.randint(0, 100)

class Materials:
    def __init__(self, name, start_index, end_index):
        self.name = name
        self.start_index = start_index
        self.end_index = end_index

gold, silver, oil, gold_needed, silver_needed, oil_needed, oxygen = 0, 0, 0, 0, 0, 0, 100
width = random.randint(20, 21)
gravity =  random.randint(0, 100)
air_pressure =  random.randint(0, 100)
materials = [
    Materials("Grass", 0, 7), 
    Materials("Stone", 8, 15),
    Materials("Water", 16, 23),
    Materials("Ice", 24, 31),
    Materials("Sand", 32, 39)
]
materials_count = 5

def planet_creator(_planet):
    j, i= 0, 0
    planet = _planet
    planet_texture = [[0 for i in range(planet.height)] for j in range(planet.width)]
    while j < planet.width:

        type_material = random.randint(1, materials_count - 1)
        rand = random.randint(2, 5)
        if j + rand >= planet.width:

            rand = planet.width - j
        while i < j + rand and i < planet.width:

            for k in range(planet.height):
                if k == 0:
                    planet_texture[i][k] = random.randint(materials[0].start_index, materials[0].end_index)
                else:
                    planet_texture[i][k] = random.randint(materials[type_material].start_index, materials[type_material].end_index)
            i += 1
        j = i
        print(planet_texture)

    return planet_texture
class Planet_return_type:
    def __init__(self):
        self.Planet = Planet()
        self.Materials = Materials
        self.materials = materials
        self.materials_count = materials_count
        self.planet_array = planet_creator(self.Planet)

# if gold >= gold_needed and silver >= silver_needed and oil >= oil_needed:
#     planet_creator()
#     if air_pressure > 80:
#         while oxygen > 0:
#             oxygen -= oxygen
#             time.sleep(1)
#     elif air_pressure > 60:
#         while oxygen > 0:
#             oxygen -= oxygen
#             time.sleep(2)
#     elif air_pressure > 40:
#         while oxygen > 0:
#             oxygen -= oxygen
#             time.sleep(3)
#     elif air_pressure <= 40:
#         while oxygen > 0:
#             oxygen -= oxygen
#             time.sleep(4)    
#     # ne znam kak raboti wurteneto na planetata trqbwa nqkoj da go naprawi kolkoto po golqma e grawitacqta tolkowa po bawmno da se wyrti planetata
#     if gravity > 75:
#         1
#     elif gravity > 50:
#         2
#     elif gravity <= 50:
#         3 # twa da e normalnoto kakto se wurti sega primerno


