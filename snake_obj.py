import pygame as pg
from pygame.math import Vector2


class Snake():
    """creates a snake object"""
    def __init__(self, game):
        self.game = game
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False


        self.body_bottomleft = pg.image.load('images/body_bottomleft.png')
        self.body_bottomright = pg.image.load('images/body_bottomright.png')

        self.body_horizontal = pg.image.load('images/body_horizontal.png')
        self.body_vertical = pg.image.load('images/body_vertical.png')

        self.body_topleft= pg.image.load('images/body_topleft.png')
        self.body_topright = pg.image.load('images/body_topright.png')

        self.head_down = pg.image.load('images/head_down.png')
        self.head_left = pg.image.load('images/head_left.png')
        self.head_right = pg.image.load('images/head_right.png')
        self.head_up = pg.image.load('images/head_up.png')

        self.tail_down = pg.image.load('images/tail_down.png')
        self.tail_left = pg.image.load('images/tail_left.png')
        self.tail_right = pg.image.load('images/tail_right.png')
        self.tail_up = pg.image.load('images/tail_up.png')



    def update_head_images(self, block_rect):
        if self.direction.x == -1 and self.direction.y == 0:
            self.game.screen.blit(self.head_left, block_rect)

        if self.direction.x == 1 and self.direction.y == 0:
            self.game.screen.blit(self.head_right, block_rect)

        if self.direction.x == 0 and self.direction.y == 1:
            self.game.screen.blit(self.head_down, block_rect)

        if self.direction.x == 0 and self.direction.y == -1:
            self.game.screen.blit(self.head_up, block_rect)



    def draw_snake(self):
        """looping over the list of the coordinates and draw rectangles"""

        for index, block in enumerate(self.body):
            x_pos = block.x * self.game.settings.cell_size
            y_pos = block.y * self.game.settings.cell_size
            block_rect = pg.Rect(x_pos, y_pos, self.game.settings.cell_size, self.game.settings.cell_size)

            if index == 0:
                self.update_head_images(block_rect)



            elif index == len(self.body) - 1:
                pre_tail = self.body[index - 1] - block


                if pre_tail.x == -1:
                    self.game.screen.blit(self.tail_right, block_rect)

                if pre_tail.x == 1:
                    self.game.screen.blit(self.tail_left, block_rect)

                if pre_tail.y == 1:
                    self.game.screen.blit(self.tail_up, block_rect)

                if pre_tail.y == -1:
                    self.game.screen.blit(self.tail_down, block_rect)



            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if previous_block.x == next_block.x:
                    self.game.screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.game.screen.blit(self.body_horizontal, block_rect)

                else:
                    if (previous_block.x == -1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == -1):
                        self.game.screen.blit(self.body_topleft, block_rect)

                    if (previous_block.x == 1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == 1):
                        self.game.screen.blit(self.body_topright, block_rect)

                    if (previous_block.y == 1 and next_block.x == -1) or (previous_block.x == -1 and next_block.y == 1):
                        self.game.screen.blit(self.body_bottomleft, block_rect)

                    if (previous_block.y == 1 and next_block.x == 1) or (previous_block.x == 1 and next_block.y == 1):
                        self.game.screen.blit(self.body_bottomright, block_rect)





    def move_snake(self):
        """
        copy the coordinates of the blocks except the last one
        update the head coordinates using a direction vector
        for example  (move up)
        before:
        [] [] [] []
        after
              []
        [] [] []
        here we copied the first 3 blocks as you can see and update the coordinates of the first block
        """
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_block(self):
        self.new_block = True
