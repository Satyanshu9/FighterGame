import pygame, random
from Constants import *
from LoadSprite import *
pygame.init()

class Thor(pygame.sprite.Sprite):
    idleFrames = []
    walkingFrames = []
    punchFrames = []
    kickFrames = []
    hitFrames = []
    deadFrames = []

    def __init__(self):
        super(Thor, self).__init__()
        self.sprite = pygame.image.load("thor_flip.png").convert_alpha()
        self.spritesheet = SpriteSheet(self.sprite)
        self.w = 250
        self.h = 300

        self.loadIdle()
        self.loadWalking()
        self.loadHitImage()
        self.loadPunchImage()
        self.loadDead()

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.ground = HEIGHT
        self.rect.x = WIDTH - 400
        self.rect.y = self.ground - self.h - 60
        self.moveX = False
        self.SPEED = 40
        self.move = 0
        self.index = 0
        self.currentMove = IDLE


    def update(self):
        if self.currentMove == MOVE:
            pass
        elif self.currentMove == KICK:
            pass
        elif self.currentMove == HIT:
            self.showHit()
        else:
            self.showIdle()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = True
            self.move = self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_LEFT]:
            self.moveX = True
            self.SPEED = 40
            self.move = -self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_UP]:
            self.isAttacking = True
            self.showPunch()
        else:
            self.move = 0
            self.showIdle()

        if self.moveX:
            self.rect.x += self.move

    def loadIdle(self):
        self.image = self.spritesheet.getImage(3398, 56, 142, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(3253, 56, 146, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(3104, 56, 150, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2943, 56, 161, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2770, 56, 172, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2604, 56, 168, 143)
        self.idleFrames.append(self.image)

    def loadWalking(self):
        self.image = self.spritesheet.getImage(3399, 1523, 142, 139)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(3254, 1523, 145, 139)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(3125, 1523, 131, 139)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(2984, 1523, 141, 139)
        self.walkingFrames.append(self.image)
    def loadDead(self):
        self.image = self.spritesheet.getImage(1963, 5647, 192, 70)
        self.deadFrames.append(self.image)
        self.image = self.spritesheet.getImage(1768, 5647, 193, 70)
        self.deadFrames.append(self.image)


    def loadHitImage(self):
        self.image = self.spritesheet.getImage(1024, 5401, 139, 124)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(1161, 5401, 143, 124)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(1305, 5401, 137, 121)
        self.hitFrames.append(self.image)
        self.image = self.spritesheet.getImage(1442, 5401, 142, 121)
        self.hitFrames.append(self.image)

    def loadPunchImage(self):
        self.image = self.spritesheet.getImage(1958, 1649, 131, 157)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(1819, 1649, 137, 159)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(1666, 1649, 151, 153)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(1502, 1649, 162, 132)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(1053, 1638, 188, 121)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(1243, 1638, 159, 138)
        self.punchFrames.append(self.image)

    def showPunch(self):
        if self.index >= len(self.punchFrames):
            self.index = 0
        self.image = self.punchFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showIdle(self):
        self.isAttacking = False
        if self.index >= len(self.idleFrames):
            self.index = 0
        self.image = self.idleFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showWalking(self):
        if self.index >= len(self.walkingFrames):
            self.index = 0
        self.image = self.walkingFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showDead(self):
        self.isAttacking = False
        if self.index >= len(self.deadFrames):
            self.index = 0
        self.image = self.deadFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showHit(self):
        if self.index >= len(self.hitFrames):
            self.index = 0
            self.currentMove = IDLE
        self.image = self.hitFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1