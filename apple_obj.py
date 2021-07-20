import pygame as pg
from pygame.math import Vector2
from random import randint

class Apple():
    """creates an apple object"""
    def __init__(self, game):
        self.game = game
        self.new_pos()
        self.apple_image = pg.image.load('images/apple.png')
        self.apple_image = pg.transform.scale(self.apple_image, (40, 40))

    def draw_apple(self):
        apple_rect = pg.Rect(self.pos.x * self.game.settings.cell_size, self.pos.y * self.game.settings.cell_size, self.game.settings.cell_size, self.game.settings.cell_size)
        self.game.screen.blit(self.apple_image, apple_rect)
        # pg.draw.rect(self.game.screen, (255, 0, 0), apple_rect)

    def new_pos(self):
        self.x = randint(0, self.game.settings.cell_number - 1)
        self.y = randint(0, self.game.settings.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
