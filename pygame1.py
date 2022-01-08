import pygame
pygame.init()

#setting up the drawing window (500x500 pixels)
screen = pygame.display.set_mode([500, 500])

#will remain true as long as window is open
running = True
while running:
    for event in pygame.event.get(): #did user click close button? (event here is close button)
        if(event.type == pygame.QUIT):
            running = False

        screen.fill((255, 255, 255)) #tuple represents rgb colors of white
        # draws a circle on the screen at (250, 250) with radius of 75 and the second tuple is rgb color of blue
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        #flips the display
        pygame.display.flip()
pygame.quit() #quits