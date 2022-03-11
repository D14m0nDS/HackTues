import pygame as pg
import os
import random
import time

pg.init()

class Planet:
    def __init__(self, width, hight, gravity, air_pressure):
        self.width = width
        self.hight = hight
        self.gravity = gravity
        self.air_pressure = air_pressure
gold, silver, oil, gold_needed, silver_needed, oil_needed, oxygen = 0, 0, 0, 0, 0, 0, 100

width = random.randint()
hight = random.randint()
gravity = random.randint(1, 100)
air_pressure = random.randint(1, 100)

if gold >= gold_needed and silver >= silver_needed and oil >= oil_needed:
    planet = (width, hight, gravity, air_pressure)
    if air_pressure > 80:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(1)
    if air_pressure > 60:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(2)
    if air_pressure > 40:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(3)
    if air_pressure <= 40:
        while oxygen > 0:
            oxygen -= oxygen
            time.sleep(4)
