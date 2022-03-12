from test_game import Game
from controls_main import *
from basic_game import *
from window_create import Window

g = Game(actions)
window_create = Window()

while g.running:
    
    g.curr_menu.display_menu(g.display)
    g.game_loop()
    
    while g.playing:
        pass
