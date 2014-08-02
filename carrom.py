import pygame, random
# from pygame.locals import *

def draWCorners():
    pygame.draw.circle(screen, BLACK, [strikerx, strikery], strikerrad)

# Define some constants
BLACK    = (   0,   0,   0)
BROWN    = (  50,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
PI = 3.141592653
border = 70
# Set the width and height of the screen [width, height]
size = (700, 700)
strikerrad = 20
strikerx = 350
strikery = 350
pocketrad = 25
svelx = 3
svely = 5
friction = 1
fps = 100;

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Carrom")

done = False    # loop till close button clicked
clock = pygame.time.Clock()

background = pygame.image.load('data/back.jpg').convert()

# main screen creation
screen.blit(background, (0, 0))
pygame.draw.rect(screen, BROWN, [0, 0, size[0], size[0]], border)
pygame.display.update()


while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, BROWN, [0, 0, size[0], size[0]], border)
    
    if fps>0:
        strikerx += svelx
        strikery += svely
        # fps -= friction
    if strikery > size[0]-border/2-strikerrad or strikery < border/2+strikerrad:
        svely = svely * -1
    if strikerx > size[0]-border/2-strikerrad or strikerx < border/2+strikerrad:
        svelx = svelx * -1

    pygame.draw.circle(screen, BLUE, [strikerx, strikery], strikerrad)
    pygame.draw.circle(screen, BLACK, [strikerx, strikery], strikerrad, 2)
    
    pygame.display.flip()
    # Limit to input frames per second
    clock.tick(fps)

pygame.quit()