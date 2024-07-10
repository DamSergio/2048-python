from settings import *
from random import randint


LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class Board:
    def __init__(self) -> None:
        self.cols = COLS
        self.rows = ROWS

        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.init_board()

    def check_lose(self) -> bool:
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] == 0:
                    return False

                if (
                    col + 1 < self.cols
                    and self.matrix[row][col] == self.matrix[row][col + 1]
                ):
                    return False

                if (
                    row + 1 < self.rows
                    and self.matrix[row][col] == self.matrix[row + 1][col]
                ):
                    return False

        return True

    def check_win(self) -> bool:
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] == 2048:
                    return True

        return False

    def move_left(self) -> None:
        for row in range(self.rows):
            for col in range(1, self.cols):
                tile_value = self.matrix[row][col]
                previus_tile_value = self.matrix[row][col - 1]

                if tile_value == 0:
                    continue

                if tile_value == previus_tile_value:
                    self.matrix[row][col - 1] = tile_value * 2
                    self.matrix[row][col] = 0

                if previus_tile_value == 0:
                    self.matrix[row][col - 1] = tile_value
                    self.matrix[row][col] = 0

                    self.move_left()

    def move_right(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols - 2, -1, -1):
                tile_value = self.matrix[row][col]
                next_tile_value = self.matrix[row][col + 1]

                if tile_value == 0:
                    continue

                if tile_value == next_tile_value:
                    self.matrix[row][col + 1] = tile_value * 2
                    self.matrix[row][col] = 0

                if next_tile_value == 0:
                    self.matrix[row][col + 1] = tile_value
                    self.matrix[row][col] = 0

                    self.move_right()

    def move_up(self) -> None:
        for col in range(self.cols):
            for row in range(1, self.rows):
                tile_value = self.matrix[row][col]
                previus_tile_value = self.matrix[row - 1][col]

                if tile_value == 0:
                    continue

                if tile_value == previus_tile_value:
                    self.matrix[row - 1][col] = tile_value * 2
                    self.matrix[row][col] = 0

                if previus_tile_value == 0:
                    self.matrix[row - 1][col] = tile_value
                    self.matrix[row][col] = 0

                    self.move_up()

    def move_down(self) -> None:
        for col in range(self.cols):
            for row in range(self.rows - 2, -1, -1):
                tile_value = self.matrix[row][col]
                next_tile_value = self.matrix[row + 1][col]

                if tile_value == 0:
                    continue

                if tile_value == next_tile_value:
                    self.matrix[row + 1][col] = tile_value * 2
                    self.matrix[row][col] = 0

                if next_tile_value == 0:
                    self.matrix[row + 1][col] = tile_value
                    self.matrix[row][col] = 0

                    self.move_down()

    def init_board(self) -> None:
        for _ in range(2):
            self.add_new_tile()

    def add_new_tile(self) -> None:
        if self.check_lose():
            return

        if any(0 in row for row in self.matrix):
            row = randint(0, self.rows - 1)
            col = randint(0, self.cols - 1)

            while self.matrix[row][col] != 0:
                row = randint(0, self.rows - 1)
                col = randint(0, self.cols - 1)

            self.matrix[row][col] = 2

    def draw_number(self, window: pygame.Surface, number: int, x: int, y: int) -> None:
        pygame.draw.rect(window, TILES_COLORS[number], (x, y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(number), True, FONT_COLOR)
        text_rect = text.get_rect(center=(x + RECT_WIDTH // 2, y + RECT_HEIGHT // 2))

        window.blit(text, text_rect)

    def draw(self, window: pygame.Surface) -> None:
        for col in range(self.cols):
            for row in range(self.rows):
                x = col * RECT_WIDTH
                y = row * RECT_HEIGHT

                value = self.matrix[row][col]
                if value != 0:
                    self.draw_number(window, value, x, y)

                pygame.draw.rect(
                    window,
                    OUTLINE_COLOR,
                    (x, y, RECT_WIDTH, RECT_HEIGHT),
                    OUTLINE_THICKNESS,
                )
