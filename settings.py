import pygame

FPS = 240
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROWS = 28
COLS = 28
GRID_SIZE = 28
WIN_SIZE = 600
WIDTH = 600
HEIGHT = 600
PIXEL_SIZE = WIDTH // COLS
THICKNESS = 2

def get_font(size):
    return pygame.font.SysFont("helvetica", size)