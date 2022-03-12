import pygame as pg
from test_game import Game

g = Game()


while g.running:
    g.curr_menu.display_menu(g.display)
    g.game_loop()
    
    while g.playing:
        pass