from settings import *
from board import Board

import time


class Game:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()

        self.board = Board()

        self.win = False
        self.lose = False

        pygame.display.set_caption(WINDOW_CAPTION)

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.board.move_left()
                    self.board.add_new_tile()

                if event.key == pygame.K_RIGHT:
                    self.board.move_right()
                    self.board.add_new_tile()

                if event.key == pygame.K_UP:
                    self.board.move_up()
                    self.board.add_new_tile()

                if event.key == pygame.K_DOWN:
                    self.board.move_down()
                    self.board.add_new_tile()

    def update(self) -> None:
        if self.board.check_lose():
            self.running = False
            self.lose = True

        if self.board.check_win():
            self.running = False
            self.win = True

    def draw(self) -> None:
        self.window.fill(BACKGROUND_COLOR)

        self.board.draw(self.window)

        if self.win:
            text = FONT.render("You win!", True, FONT_COLOR)
            self.window.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    HEIGHT // 2 - text.get_height() // 2,
                ),
            )

        if self.lose:
            text = FONT.render("You lose!", True, FONT_COLOR)
            self.window.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    HEIGHT // 2 - text.get_height() // 2,
                ),
            )

        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()

            self.clock.tick(FPS)

        time.sleep(2)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
