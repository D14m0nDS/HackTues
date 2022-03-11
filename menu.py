import pygame as pg

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_width, self.mid_height = self.game.DISPLAY_WIDTH/2, self.game.DISPLAY_HEIGHT/2
        self.run_display = True
        self.cursor_rect =  pg.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        pass
        # self.cursor_rect = pg.image.load(r'D:\Downloads\programing\HackTues\images\cursor.png')

    def blit_screen(self):
        self.game.blit(self.game.display, (0,0))
        pg.display.update()
        self.game.reset_keys

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start Game"
        self.startx, self.starty =  self.mid_width, self.mid_height + 30
        self.optionsx, self.optionsy =  self.mid_width, self.mid_height + 50
        self.cretitsx, self.creditsy =  self.mid_width, self.mid_height + 50
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    
    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('MAIN MENU', 30, self.game.DISPLAY_WIDTH/2, self.game.DISPLAY_HEIGHT/2 - 20)
            self.game.draw_text('Start Game', 20, self.startx , self.starty)
            self.game.draw_text('Options', 20, self.optionsx , self.optionsy)
            self.game.draw_text('Credits', 20, self.creditsx , self.creditsy)
            self.draw_cursor()

            self.blit_screen()



    def cursor_movement(self):
        if self.game.KEY_DOWN:
            if self.state == "Start Game":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state == "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state == "Credits"
            elif self.state =="Credits":
                self.cursor_rect.midtop = (self.startx, self.offset,self.starty)
                self.state == "Start Game"
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
        self.cursor_movement()
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
        self.volx, self.voly = self.mid_width, self.mid_height + 20
        self.controlsx, self.controlsy = self.mid_width, self.mid_height + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_WEIGHT / 2, self.game.DISPLAY_HEIGHT / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()

            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
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
            self.game.draw_text('Credits', 20, self.game.DISPLAY_WEIGHT / 2, self.game.DISPLAY_HEIGHT / 2 - 20)
            self.game.draw_text('', 15, self.game.DISPLAY_WEIGHT / 2, self.game.DISPLAY_HEIGHT / 2 + 10)
            
            self.blit_screen()
    



    