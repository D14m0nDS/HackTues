from test_game import Game
# from controls_main import *
from basic_game import *
from window_create import Window

g = Game()
window_create = Window()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    
    while g.playing:
        basic_game
