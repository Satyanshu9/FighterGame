
import pygame
from Constants import *
from Game import *
from PlayerHulk import *
from PlayerThor import *
from PlayerHealth import *
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)

def main():

    bgImage = pygame.image.load("thor_wins.jpg")
    bgImage = pygame.transform.scale(bgImage, SIZE)
    font = pygame.font.SysFont(None, 200)
    text = font.render("THOR WINS", True, GREEN)
    SCREEN.blit(text, (WIDTH // 2 - 400, HEIGHT // 2 - 50))

    SCREEN.blit(bgImage, (0, 0))

    pygame.display.flip()
    font = pygame.font.SysFont(None, 200)
    text = font.render("THOR WINS", True, GREEN)
    SCREEN.blit(text, (WIDTH // 2 - 400, HEIGHT // 2 - 50))
    pygame.display.flip()


main()