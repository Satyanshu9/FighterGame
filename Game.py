import pygame, random

import hulkWins
import thorWins
from Constants import *
from PlayerHulk import *
from PlayerThor import *
from PlayerHealth import *
from pygame.locals import *
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)
# SCREEN = pygame.display.set_mode()

sprite_group = pygame.sprite.Group()
hulk = Hulk()
sprite_group.add(hulk)

thor = Thor()
sprite_group.add(thor)

hulkSprite = pygame.sprite.Group()
hulkSprite.add(hulk)

thorSprite = pygame.sprite.Group()
thorSprite.add(thor)
healthWidth = WIDTH//2 - 100

hulkHealth = Health("HULK", 10, 10, healthWidth, 50)
thorHealth = Health("THOR", WIDTH - healthWidth - 10, 10, healthWidth, 50)
restHealth = Health("HULK", 10, 10, healthWidth, 50)
def drawHealth():
    restHealth.restHealthHulk(SCREEN)
    hulkHealth.showHealth(SCREEN)

    hulkHealth.showName(SCREEN)

    thorHealth.showHealth(SCREEN)
    thorHealth.showName(SCREEN)

def showTimer(time_left):
    font = pygame.font.SysFont(None, 100)
    text = font.render(f"{time_left}", True, RED)
    SCREEN.blit(text, (WIDTH//2 - 40, 10))

def main():
    bgImage = pygame.image.load("bg4.jpg")

    clock = pygame.time.Clock()
    FPS = 10

    pygame.time.set_timer(USEREVENT + 1, 1000)
    seconds = 60

    hulkHealth.restHealthHulk(SCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT + 1:
                if seconds > 0:
                    seconds -= 1


        SCREEN.blit(bgImage, (0, -120))

        if seconds < 1:
            font = pygame.font.SysFont(None, 200)
            text = font.render("TIME OVER", True, RED)
            SCREEN.blit(text, (WIDTH // 2 - 400, HEIGHT // 2 - 50))



        if pygame.sprite.groupcollide(hulkSprite, thorSprite, False, False):

            if hulk.isAttacking:
                bgMusic = pygame.mixer.Sound("punch1.mp3")
                bgMusic.play(0)
                thor.currentMove = HIT
                thor.showHit()
                thorHealth.rect_2.w += 10

            if thor.isAttacking:
                bgMusic = pygame.mixer.Sound("punch2.mp3")
                bgMusic.play(0)
                hulk.currentMove = HIT
                hulk.showHit()
                hulkHealth.rect.w -= 10

            print("Collision Detection")
            hulk.moveX = False
            hulk.SPEED = 0

        if hulkHealth.rect.w < 15:
            hulk.showDead()
            thorWins.main()
        if thorHealth.rect_2.w > 580:
            thor.showDead()
            hulkWins.main()

        drawHealth()
        showTimer(seconds)
        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

# main()