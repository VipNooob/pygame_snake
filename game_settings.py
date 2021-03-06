import pygame as pg

class Settings():
    def __init__(self):
        self.start_condition = False
        self.game_condition = True
        self.win_condition = False


        pg.mouse.set_visible(True)

        self.cell_size = 40
        self.cell_number = 20 + 1

        self.cell_row_number = 23
        self.cell_column_number = 21

        self.pixel_font_1 = pg.font.Font('pixel_font/Minecraft.ttf', 110)
        self.pixel_font_2 = pg.font.Font('pixel_font/Minecraft.ttf', 90)

        self.pixel_font_3 = pg.font.Font('pixel_font/Minecraft.ttf', 60)

        self.pixel_font_winner = pg.font.Font('pixel_font/Minecraft.ttf', 80)


        self.delay = pg.USEREVENT
        self.score = 0

        with open('record_score.txt', 'r') as file:
            self.record = file.read()
