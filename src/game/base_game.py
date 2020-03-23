from pygame.locals import *
import pygame
import sys
from pygame import mixer


class BaseGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def make_window(self):
        pygame.init()
        screen = pygame.display.set_mode(self.height, self.width)
        pygame.display.set_caption()

    def run(self):
        try:
            while True:
                pygame.draw.rect(screen, (255, 255, 0), Rect(10, 10, 20, 50))
                pygame.display.update()

        except SyntaxError:
            pass
        finally:
            sys.exit()


game = BaseGame(600, 400)
game.make_window()
