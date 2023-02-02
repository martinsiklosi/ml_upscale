import pygame

FPS = 240
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
IN_SIZE = 20
ROWS = IN_SIZE
COLS = IN_SIZE
OUT_SIZE = 45
WIN_SIZE = 600
WIDTH = 600
HEIGHT = 600
PIXEL_SIZE = WIDTH // COLS
THICKNESS = 2

def get_font(size):
    return pygame.font.SysFont("helvetica", size)