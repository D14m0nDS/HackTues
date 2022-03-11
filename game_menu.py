import pygame as pg


class Game():
    def __init__(self):
        pg.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 480, 270
        self.display = pg.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.window = pg.display.set_mode(((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)))
        
        pg.display.set_caption("GAME MENU")

        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0,0,0), (255, 255, 255)

    def game_loop(self):
        while self.playing:
            pg.time.delay(100)
            self.event_checking()
            if self.START_KEY:
                self.playing = False
            
            self.display.fill(self.BLACK)
            self.draw_text("NOT WORKING!!!", 20, self.DISPLAY_WIDTH/2, self.DISPLAY_HEIGHT/2)
            self.window.blit(self.display, (0,0))
            
            pg.display.update()
            self.keys_reset()

    def event_checking(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running, self.playing = False, False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.START_KEY = True
                if event.key == pg.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pg.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pg.K_UP:
                    self.UP_KEY = True
    
    def keys_reset(self):
        self.START_KEY, self.BACK_KEY, self.K_DOWN, self.K_UP = False, False, False, False
    def draw_text(self, text, size, x, y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)