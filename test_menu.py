import pygame as pg, sys
import os, json
from save_load import load_save, reset_keys
from control_settings import Controls_Handler


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pg.Rect(-100, 0, 0, 0)
        self.offset = - 100

    def draw_cursor(self, surface):
        color = (255,13,5) if self.selected else (255,250,239)
        pg.draw.rect(surface, color, (80 , 270/4 - 10 + (self.curr_index*30), 320, 20) )
        # self.cursor_rect = pg.image.load(r'./images/cursor.png')

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pg.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start Game"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('MAIN MENU', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Start Game", 25, self.startx, self.starty)
            self.game.draw_text("Options", 25, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 25, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start Game':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start Game'
        elif self.game.UP_KEY:
            if self.state == 'Start Game':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start Game'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start Game':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 30
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 60
        self.backx, self.backy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('OPTIONS', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Volume", 25, self.volx, self.voly)
            self.game.draw_text("Controls", 25, self.controlsx, self.controlsy)
            self.game.draw_text("Back", 25, self.backx, self.backy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY: 
            if self.state == 'Volume':
                self.state = 'Back'
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
            elif self.state == 'Back':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
        elif self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Back'
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy)
            elif self.state == 'Back':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
    
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Volume':
                pass
            elif self.state == 'Controls':
                pass
            elif self.state == 'Back':
                self.game.curr_menu = self.game.main_menu
            self.run_display = False
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('CREDITS', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text('MADE BY:', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        pass

class ControlMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self,game)
    
    def display_menu():
        pass
    def move_cursor(self, Menu, Game):
        pass
 

