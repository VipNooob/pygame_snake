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
        while True:
            counter = 0
            self.x = randint(1, self.game.settings.cell_column_number - 2)
            self.y = randint(3, self.game.settings.cell_row_number - 2)
            for part in self.game.snake.body:
                if self.x == part.x and self.y == part.y:
                    counter += 1
                    break
            if counter == 0:
                break


        self.pos = Vector2(self.x, self.y)
