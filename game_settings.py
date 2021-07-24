import pygame as pg

class Settings():
    def __init__(self):
        self.cell_size = 40
        self.cell_number = 20 + 1

        self.cell_row_number = 23
        self.cell_column_number = 21


        self.delay = pg.USEREVENT

        self.score = 0

        with open('record_score.txt', 'r') as file:
            self.record = file.read()
