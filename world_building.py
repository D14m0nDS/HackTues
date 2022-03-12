import pygame as pg
import os
import random
import time

class Planet:
    def __init__(self, width, hight, gravity, air_pressure):
        self.width = width
        self.hight = hight
        self.gravity = gravity
        self.air_pressure = air_pressure

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
    Materials("Water", 0, 5), 
    Materials("Stone", 6, 10),
    Materials("Water", 11, 15),
]
materials_count = 3

def planet_creator():
    j, i= 0, 0

    planet = Planet(width, 5, gravity, air_pressure)
    planet_texture = [[0 for i in range(planet.hight)] for j in range(planet.width)]
    while j < planet.width:

        type_material = random.randint(0, materials_count - 1)
        rand = random.randint(2, 5)
        if j + rand >= planet.width:

            rand = planet.width - j
        while i < j + rand and i < planet.width:

            for k in range(planet.hight):

                print(f"x {i}")
                print(f"y {k}")
                planet_texture[i][k] = random.randint(materials[type_material].start_index, materials[type_material].end_index)
            i += 1
        j = i
        print(planet_texture)

    print(planet_texture)

if gold >= gold_needed and silver >= silver_needed and oil >= oil_needed:
    planet_creator()
    if air_pressure > 80:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(1)
    elif air_pressure > 60:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(2)
    elif air_pressure > 40:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(3)
    elif air_pressure <= 40:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(4)    
    # ne znam kak raboti wurteneto na planetata trqbwa nqkoj da go naprawi kolkoto po golqma e grawitacqta tolkowa po bawmno da se wyrti planetata
    if gravity > 75:
        1
    elif gravity > 50:
        2
    elif gravity <= 50:
        3 # twa da e normalnoto kakto se wurti sega primerno

