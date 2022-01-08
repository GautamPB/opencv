import pygame
pygame.init()

screen = pygame.display.set_mode([500, 480])
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.walkCount = 0
        self.jumpCount = 10
        self.left = False
        self.right = False

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(char, (self.x, self.y))

clock = pygame.time.Clock()

running = True

man = Player(300, 410, 64, 64)

def redrawGameWindow():
    screen.blit(bg, (0, 0))
    man.draw(screen)
    pygame.display.update()

while(running):
    clock.tick(27)
    pygame.time.delay(50)  # time is in milliseconds
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and man.x > 10):
        man.x -= man.vel
        man.left = True
        man.right = False
    elif(keys[pygame.K_RIGHT] and man.x < 490 - man.width):
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.left = False
        man.right = False
        man.walkCount = 0

    if(man.isJump == False):
        if(keys[pygame.K_SPACE]):
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if(man.jumpCount >= -10):
            neg = 1
            if(man.jumpCount < 0):
                neg = -1
            man.y -= int((man.jumpCount ** 2) * 0.5 * neg)
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()
pygame.quit()