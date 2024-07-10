import pygame
import sys


pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 800
WINDOW_CAPTION = "2048"

FONT = pygame.font.SysFont("comicsans", 60, bold=True)

# Board settings
ROWS, COLS = 4, 4
RECT_WIDTH = WIDTH // COLS
RECT_HEIGHT = HEIGHT // ROWS

# Colors
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

TILES_COLORS = {
    2: (237, 229, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 101),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 99),
    512: (236, 202, 80),
    1024: (237, 200, 80),
    2048: (237, 197, 63),
}

# Game
FPS = 60
MOVE_VELOCITY = 20
