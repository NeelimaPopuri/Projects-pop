import time
import random
import math
import pygame
pygame.__version__
pygame.init()

WIDTH, HEIGTH = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("AIM TRAINER")


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.QUIT()


if __name__ == "__main__":
    main()
