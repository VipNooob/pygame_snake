import sys
import pygame as pg
from game_settings import Settings
from apple_obj import Apple
from snake_obj import Snake
from pygame.math import Vector2

pg.init()


class Game:
    """create a game structure"""

    def __init__(self):
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.cell_column_number * self.settings.cell_size, self.settings.cell_row_number * self.settings.cell_size))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()


        self.apple = Apple(self)
        self.snake = Snake(self)

        self.test_surface = pg.Surface((100, 200))
        self.test_surface.fill((0, 0, 255))


        self.x = 0
        self.y = 0
        self.pos = Vector2(self.x, self.y)
        self.cell_rect = pg.Rect(self.pos.x * self.settings.cell_size, self.pos.y * self.settings.cell_size, self.settings.cell_size, self.settings.cell_size)

        pg.time.set_timer(self.settings.delay, 100)


    def check_collision(self):
        """check the collision between a snake head and an apple"""
        if self.apple.pos == self.snake.body[0]:
            self.apple.new_pos()
            self.snake.add_block()


    def check_fail(self):
        """
        check a collisions between
        1. snake and canvas limits
        2. snake parts
        """
        # left-right condition
        if self.snake.body[0].x < 1 or self.snake.body[0].x >= self.settings.cell_column_number - 1:
            pg.quit()
            self.game_over()

        #top-bottom condition
        if self.snake.body[0].y < 3 or self.snake.body[0].y >= self.settings.cell_row_number -1:
            pg.quit()
            self.game_over()


        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()




    def _draw_external_canvas(self):
        """
        draw a place for the current score and max score
        draw game borders
        """
        info_part = pg.Rect(0, 0, self.settings.cell_size * self.settings.cell_column_number,
                            self.settings.cell_size * 2)
        pg.draw.rect(self.screen, (74, 117, 44), info_part)

        # draw an external square (borders)
        upper_part = pg.Rect(0, 2 * self.settings.cell_size, self.settings.cell_size * self.settings.cell_column_number,
                             self.settings.cell_size)
        pg.draw.rect(self.screen, (87, 138, 52), upper_part)

        lower_part = pg.Rect(0, (self.settings.cell_row_number - 1) * self.settings.cell_size,
                             self.settings.cell_size * self.settings.cell_column_number, self.settings.cell_size)
        pg.draw.rect(self.screen, (87, 138, 52), lower_part)

        left_part = pg.Rect(0, 3 * self.settings.cell_size, self.settings.cell_size,
                            (self.settings.cell_row_number - 4) * self.settings.cell_size)
        pg.draw.rect(self.screen, (87, 138, 52), left_part)

        right_part = pg.Rect((self.settings.cell_column_number - 1) * self.settings.cell_size,
                             3 * self.settings.cell_size, self.settings.cell_size,
                             (self.settings.cell_row_number - 4) * self.settings.cell_size)
        pg.draw.rect(self.screen, (87, 138, 52), right_part)


    def draw_canvas(self):
        self._draw_external_canvas()

        # draw a pattern on the canvas
        for i in range(3, self.settings.cell_row_number - 1):

            for k in range(1, self.settings.cell_column_number - 1):

                # set a new coordinates of a cell
                self.cell_rect.x = k * self.settings.cell_size
                self.cell_rect.y = i * self.settings.cell_size




                if i % 2 == 0:
                    if k % 2 == 0:
                        rgb = (162, 209, 73)
                    else:
                        rgb = (175, 215, 70)
                else:
                    if k % 2 == 0:
                        rgb = (175, 215, 70)
                    else:
                        rgb = (162, 209, 73)

                pg.draw.rect(self.screen, rgb, self.cell_rect)



    def start_game(self):
        """run the game"""
        while True:
            for event in pg.event.get():

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0, -1)

                    if event.key == pg.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0, 1)

                    if event.key == pg.K_RIGHT:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1, 0)

                    if event.key == pg.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1, 0)


                if event.type == pg.QUIT:
                    sys.exit()

                if event.type == self.settings.delay:
                    self.snake.move_snake()
                    self.check_collision()


            self.draw_canvas()

            self.apple.draw_apple()

            self.snake.draw_snake()
            self.check_fail()
            pg.display.update()
            self.clock.tick(60)


    def game_over(self):
        sys.exit()


if __name__ == '__main__':
    snake = Game()
    snake.start_game()
